import csv
import json
import statistics
from collections import defaultdict, OrderedDict
from utils.dates import convert_datetime
from utils.encoding import DecimalEncoder

class EventManager:
    def __init__(self, **kwargs):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def max_earthquakes_location(self):
        """Return the location with most earthquakes"""
        return statistics.mode([e.locationSource for e in self.events])

    def daily_histogram(self, tz='UTC'):
        """
        Return mode for each day
        """
        days = defaultdict(int)
        for e in self.events:
            date = convert_datetime(e.time, target_format='%Y-%m-%d', target_tz=tz)
            days[date] += 1

        ordered_dates = OrderedDict(sorted(days.items(), key=lambda dt: dt[0]))
        return json.dumps(ordered_dates)


class SeismicEvent:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class EarthquakeEvent(SeismicEvent):
    EVENT_TYPE = 'earthquake'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return json.dumps(self.__dict__)


def get_filtered_headings(headings_list, select_headings):
    heading_indices = [(heading, headings.index(heading)) for heading in headings_list]
    filtered = list(filter(lambda x: x[0] in select_headings, heading_indices))
    return dict((x,y) for x,y in filtered)


if __name__ == '__main__':

    DATA_SOURCE = 'data/1.0_month.csv'
    TARGET_TZ = 'America/Los_Angeles'

    FILTER_FIELD = 'type'
    FILTER_VALUE = 'earthquake'

    SELECT_HEADINGS = ['time', 'locationSource', 'mag', 'type']

    manager = EventManager()

    with open(DATA_SOURCE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headings = next(reader)

        filtered = get_filtered_headings(headings, SELECT_HEADINGS)

        for row in reader:
            attributes = {}
            for key in filtered.keys():
                # Skip the rows with fields we don't want
                filter_index = filtered[FILTER_FIELD]
                if row[filter_index] != FILTER_VALUE:
                    break
                index = filtered[key]
                attributes[key] = row[index]

            if attributes:
                e = EarthquakeEvent(**attributes)
                manager.add_event(e)

        print(manager.max_earthquakes_location())
        print(manager.daily_histogram(timezone='America/Los_Angeles'))
