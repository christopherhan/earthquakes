import csv
import json
from dateutil import parser
from dateutil import tz
from collections import defaultdict, OrderedDict
from datetime import datetime

def convert_datetime(date_str, target_format='%Y-%m-%d', target_tz=None):
    """
    Converts an ISO8601 formatted string to a target format and optional target timezone.
    """

    d = parser.isoparse(date_str)
    if target_tz:
        utc = d.replace(tzinfo=tz.gettz('UTC'))
        d = utc.astimezone(tz.gettz(target_tz))

    converted = d.strftime(target_format)

    return converted


class Earthquake:

    def __init__(self, datetime_occurred=None, event_type=None, location_source=None):
        self.datetime_occurred = datetime_occurred
        self.location_source = location_source
        self.event_type = event_type


if __name__ == '__main__':

    DATA_SOURCE = 'data/1.0_month.csv'
    EVENT_TYPE = 'earthquake'
    TARGET_TZ = 'America/Los_Angeles'

    location_counts = defaultdict(int)
    date_counts = defaultdict(int)

    with open(DATA_SOURCE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for row in reader:
            occurred = convert_datetime(row[0], target_tz=TARGET_TZ)
            event_type = row[14]
            location_source = row[20]

            if event_type != EVENT_TYPE:
                continue

            eq = Earthquake(datetime_occurred=occurred, event_type=event_type,
                            location_source=location_source)

            location_counts[eq.location_source] += 1
            date_counts[eq.datetime_occurred] += 1

    if location_counts:
        print('Location source with most %s in 30 days: %s' % (EVENT_TYPE,
              max(location_counts, key=location_counts.get)))
    else:
        print('No event types matched.')

    if date_counts:
        ordered_dates = OrderedDict(sorted(date_counts.items(), key=lambda dt: dt[0]))
        print('Number of occurrences per date: %s' % json.dumps((ordered_dates)))
    else:
        print('No occurrences found.')
