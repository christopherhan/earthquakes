import sys
import csv
import json
from collections import defaultdict, OrderedDict
from decimal import Decimal

from utils.dates import convert_datetime
from utils.encoding import DecimalEncoder

class AverageMagnitude:
    locations = {}

    @classmethod
    def callback(cls, data):
        magnitude = data[4].strip()
        location = data[20].strip()

        if location not in cls.locations:
            cls.locations[location] = {}

        if 'average' in cls.locations[location]:
            average = cls.locations[location]['average']
        else:
            average = cls.locations[location]['average'] = Decimal('0.00')

        if 'count' in cls.locations[location]:
            count = cls.locations[location]['count']
        else:
            count = cls.locations[location]['count'] = 0

        cls.locations[location]['count'] = count+1
        # Cannot store sum. average=sum/count. Therefore sum=average*count
        cls.locations[location]['average'] = ((average*count) + Decimal(magnitude)) / (count+1)

        del magnitude, location, count, average

    @classmethod
    def query(cls, location):
        try:
            return { 'average': str(round(cls.locations[location]['average'], 2)),
                     'count': cls.locations[location]['count'] }
        except KeyError:
            return { 'message': 'locationSource does not exist' }



class Earthquake:

    def __init__(self, date_occurred=None, event_type=None, location_source=None,
                 magnitude=None):
        self.date_occurred = date_occurred
        self.location_source = location_source
        self.event_type = event_type
        self.magnitude = magnitude

    def __str__(self):
        return (f'Date Occured: {self.date_occurred}\n'
                f'Location Source: {self.location_source}\n'
                f'Magnitude: {self.magnitude}\n'
                f'Event Type: {self.event_type}')

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'date_occurred={self.date_occurred}, '
                f'location_source={self.location_source}, '
                f'magnitude={self.magnitude}, '
                f'event_type={self.event_type})')

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

            eq = Earthquake(date_occurred=occurred,
                            magnitude=magnitude,
                            event_type=event_type,
                            location_source=location_source)

            location_counts[eq.location_source] += 1
            date_counts[eq.date_occurred] += 1
            total_magnitudes[eq.location_source] += magnitude

            location_magnitudes[eq.location_source] = (total_magnitudes[eq.location_source]
                                                       / location_counts[eq.location_source])

            # Simulate callback being invoked for Question 4
            AverageMagnitude.callback(row)

    print('############ Question 1 ############')
    if location_counts:
        print('Which location source had the most %s(s)?: %s' % (EVENT_TYPE,
              max(location_counts, key=location_counts.get)), '\n')
    else:
        print('No event types matched.', '\n')

    print('############ Question 2 ############')
    if date_counts:
        ordered_dates = OrderedDict(sorted(date_counts.items(), key=lambda dt: dt[0]))
        zone = TARGET_TZ if TARGET_TZ else 'UTC'
        print('Occurrences per date (%s): %s' % (zone, json.dumps((ordered_dates))), '\n')
    else:
        print('No occurrences found.', '\n')

    print('############ Question 3 ############')
    if location_magnitudes:
        print('Average magnitudes per location: %s' %
              json.dumps(location_magnitudes, cls=DecimalEncoder), '\n')
    else:
        print('No magnitudes available.', '\n')

    print('############ Question 4 ############')
    print("Querying location 'ak': ", AverageMagnitude.query('ak'))
    print("Querying location 'ci': ", AverageMagnitude.query('ci'))
    print("Querying location 'hv': ", AverageMagnitude.query('hv'))
