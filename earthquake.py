import csv
from collections import defaultdict

DATA_SOURCE = 'data/1.0_month.csv'
EVENT_TYPE = 'earthquakes'

class Earthquake:

    def __init__(self, time_since_epoch=None, event_type=None, location_source=None):
        self.time_since_epoch = time_since_epoch
        self.location_source = location_source
        self.event_type = event_type

if __name__ == '__main__':

    location_counts = defaultdict(int)

    with open(DATA_SOURCE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for row in reader:
            time = row[0]
            event_type = row[14]
            location_source = row[20]

            if event_type != EVENT_TYPE:
                continue

            eq = Earthquake(time_since_epoch=time, event_type=event_type,
                            location_source=location_source)

            location_counts[eq.location_source] += 1

    if location_counts:
        print('Location source with most %s in 30 days: %s' % (EVENT_TYPE,
              max(location_counts, key=location_counts.get)))
    else:
        print('No event types matched')
