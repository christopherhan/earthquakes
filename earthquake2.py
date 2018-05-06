import json
import statistics
from decimal import Decimal
from collections import defaultdict, OrderedDict
from utils.dates import convert_datetime

class EventManager:
    def __init__(self, **kwargs):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def max_earthquakes_location(self):
        """Return the location with most earthquakes"""
        return statistics.mode([e.locationSource for e in self.events])

    def daily_histogram(self, target_tz='UTC'):
        """Return frequency for each day"""
        days = defaultdict(int)
        for e in self.events:
            date = convert_datetime(e.time, target_format='%Y-%m-%d',
                                    target_tz=target_tz)
            days[date] += 1

        ordered_dates = OrderedDict(sorted(days.items(), key=lambda dt: dt[0]))
        return ordered_dates

    def average_magnitude_location(self, location):
        """Calculate the average magnitude for a given location"""

        magnitudes = [Decimal(e.mag) for e in list(
            filter(lambda x: x.locationSource == location, self.events))]
        return {location: round(statistics.mean(magnitudes), 2)}

    def average_magnitude_locations(self):
        """Calculate the average magnitude for all locations"""
        locs = {}
        for e in self.events:
            if e.locationSource in locs:
                locs[e.locationSource]['magnitudes'].append(Decimal(e.mag))
            else:
                locs[e.locationSource] = {
                    'magnitudes': [Decimal(e.mag)],
                    'avg': Decimal('0.00')
                }

        for key in locs:
            magnitudes = locs[key]['magnitudes']
            locs[key]['avg'] = statistics.mean(magnitudes)

        return {key: round(locs[key]['avg'], 2) for key in locs}

class SeismicEvent:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class EarthquakeEvent(SeismicEvent):
    EVENT_TYPE = 'earthquake'

    def __str__(self):
        return json.dumps(self.__dict__)
