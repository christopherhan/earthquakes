import csv
import json
from collections import defaultdict, OrderedDict
from decimal import Decimal
from earthquake import Earthquake, AverageMagnitude

from utils.dates import convert_datetime
from utils.encoding import DecimalEncoder

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

            magnitude = Decimal(row[4].strip())
            location_source = row[20].strip()
            occurred = convert_datetime(row[0].strip(),
                                        target_format='%Y-%m-%d',
                                        target_tz=TARGET_TZ)

            eq = Earthquake(date_occurred=occurred,
                            magnitude=magnitude,
                            event_type=event_type,
                            location_source=location_source)

            location_counts[eq.location_source] += 1
            date_counts[eq.date_occurred] += 1
            total_magnitudes[eq.location_source] += magnitude

            location_magnitudes[eq.location_source] = (total_magnitudes[eq.location_source]
                                                       / location_counts[eq.location_source])

            # Question 4. Simulate callback being invoked
            AverageMagnitude.callback(row)

    if location_counts:
        out = 'Which location source had the most %s(s)?: %s' % (EVENT_TYPE,
              max(location_counts, key=location_counts.get))
    else:
        out = 'No event types matched.'

    print(out)

    if date_counts:
        ordered_dates = OrderedDict(sorted(date_counts.items(), key=lambda dt: dt[0]))
        zone = TARGET_TZ if TARGET_TZ else 'UTC'
        out = 'Occurrences per date (%s): %s' % (zone, json.dumps((ordered_dates)))
    else:
        out = 'No occurrenes found.'

    print(out)

    if location_magnitudes:
        out = ('Average magnitudes per location: %s' %
              json.dumps(location_magnitudes, cls=DecimalEncoder))
    else:
        out = 'No magnitudes available.'

    print(out)

    # Question 4
    print("Average magnitude for 'ak': ", AverageMagnitude.query('ak'))
    print("Average magnitude for 'ci': ", AverageMagnitude.query('ci'))
