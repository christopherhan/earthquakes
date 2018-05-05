import csv
import json
from collections import defaultdict, OrderedDict
from datetime import datetime
from decimal import Decimal

from utils.dates import convert_datetime
from utils.encoding import DecimalEncoder

class AverageMagnitude:
    LOCATIONS = {}

    @classmethod
    def callback(cls, data):
        magnitude = data[4]
        location = data[20].strip()

        if location not in cls.LOCATIONS:
            cls.LOCATIONS[location] = {}

        if 'average' in cls.LOCATIONS[location]:
            average = cls.LOCATIONS[location]['average']
        else:
            average = cls.LOCATIONS[location]['average'] = Decimal('0.00')

        if 'count' in cls.LOCATIONS[location]:
            count = cls.LOCATIONS[location]['count']
        else:
            count = cls.LOCATIONS[location]['count'] = 0

        cls.LOCATIONS[location]['count'] = count+1
        # Cannot store sum. average=sum/count. Therefore sum=average*count
        cls.LOCATIONS[location]['average'] = ((average*count) + Decimal(magnitude)) / (count+1)

        del magnitude, location, count, average

    @classmethod
    def query(cls, location):
        try:
            return { 'average': str(round(cls.LOCATIONS[location]['average'], 2)),
                     'count': cls.LOCATIONS[location]['count'] }
        except KeyError:
            return { 'message': 'locationSource does not exist' }



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

            event_type = row[14].strip()

            if event_type != EVENT_TYPE:
                continue

            occurred = convert_datetime(row[0].strip(), target_tz=TARGET_TZ)
            magnitude = Decimal(row[4].strip())
            location_source = row[20].strip()

            eq = Earthquake(datetime_occurred=occurred,
                            magnitude=magnitude,
                            event_type=event_type,
                            location_source=location_source)

            location_counts[eq.location_source] += 1
            date_counts[eq.datetime_occurred] += 1
            total_magnitudes[eq.location_source] += magnitude

            location_magnitudes[eq.location_source] = (total_magnitudes[eq.location_source]
                                                       / location_counts[eq.location_source])

            # Simulate callback being invoked
            AverageMagnitude.callback(row)

    # Question 1
    if location_counts:
        print('Which location source had the most %s(s)?: %s' % (EVENT_TYPE,
              max(location_counts, key=location_counts.get)))
    else:
        print('No event types matched.')

    # Question 2
    if date_counts:
        ordered_dates = OrderedDict(sorted(date_counts.items(), key=lambda dt: dt[0]))
        print('Occurrences per date: %s' % json.dumps((ordered_dates)))
    else:
        print('No occurrences found.')

    # Question 3
    if location_magnitudes:
        print('Average magnitudes per location: %s' %
              json.dumps(location_magnitudes, cls=DecimalEncoder))
    else:
        print('No magnitudes available.')

    # Question 4
    print("Querying location 'ak': ", AverageMagnitude.query('ak'))
    print("Querying location 'ci': ", AverageMagnitude.query('ci'))
    print("Querying location 'hv': ", AverageMagnitude.query('hv'))
