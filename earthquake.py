import csv
import json
from dateutil import parser
from dateutil import tz
from collections import defaultdict, OrderedDict
from datetime import datetime
from decimal import Decimal

from utils.dates import convert_datetime
from utils.encoding import DecimalEncoder

class Earthquake:

    def __init__(self, datetime_occurred=None, event_type=None, location_source=None,
                 magnitude=None):
        self.datetime_occurred = datetime_occurred
        self.location_source = location_source
        self.event_type = event_type
        self.magnitude = magnitude


if __name__ == '__main__':

    DATA_SOURCE = 'data/1.0_month.csv'
    EVENT_TYPE = 'earthquake'
    TARGET_TZ = 'America/Los_Angeles'

    location_magnitudes = {}
    location_counts = defaultdict(int)
    total_magnitudes = defaultdict(Decimal)
    date_counts = defaultdict(int)

    with open(DATA_SOURCE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for row in reader:

            event_type = row[14]

            if event_type != EVENT_TYPE:
                continue

            occurred = convert_datetime(row[0], target_tz=TARGET_TZ)
            magnitude = Decimal(row[4])
            location_source = row[20]

            eq = Earthquake(datetime_occurred=occurred,
                            magnitude=magnitude,
                            event_type=event_type,
                            location_source=location_source)

            location_counts[eq.location_source] += 1
            date_counts[eq.datetime_occurred] += 1
            total_magnitudes[eq.location_source] += magnitude

            location_magnitudes[eq.location_source] = (total_magnitudes[eq.location_source]
                                                       / location_counts[eq.location_source])

    if location_counts:
        print('Which location source had the most %s(s)?: %s' % (EVENT_TYPE,
              max(location_counts, key=location_counts.get)))
    else:
        print('No event types matched.')

    if date_counts:
        ordered_dates = OrderedDict(sorted(date_counts.items(), key=lambda dt: dt[0]))
        print('Occurrences per date: %s' % json.dumps((ordered_dates)))
    else:
        print('No occurrences found.')

    if location_magnitudes:
        print('Average magnitudes per location: %s' %
              json.dumps(location_magnitudes, cls=DecimalEncoder))
    else:
        print('No magnitudes available.')
