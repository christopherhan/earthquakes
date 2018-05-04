import csv

DATA_SOURCE = 'data/1.0_month.csv'

class Earthquake:

    SEISMIC_EVENT_TYPES = ['earthquake', 'explosion', 'quarry_blast', 'ice quake',
                           'chemical explosion', 'mining explosion', 'other_event']

    def __init__(self, time_since_epoch=None, event_type=None, location_source=None):
        self.time_since_epoch = time_since_epoch
        self.location_source = location_source
        self.event_type = event_type

if __name__ == '__main__':
    with open(DATA_SOURCE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            time = row[0]
            event_type = row[14]
            location_source = row[20]

            if event_type != 'earthquake':
                continue

            eq = Earthquake(time_since_epoch=time, event_type=event_type,
                            location_source=location_source)

            print(eq.time_since_epoch, eq.event_type, eq.location_source)
