import json
import statistics
from decimal import Decimal
from collections import defaultdict, OrderedDict
from utils.dates import convert_datetime

class SeismicEvent:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        attributes = []
        for key, value in self.__dict__.items():
            attributes.append(f'{key}: {value}')
        return ', '.join(attributes)

    def __repr__(self):
        return json.dumps(self.__dict__)

class EarthquakeEvent(SeismicEvent):
    EVENT_TYPE = 'earthquake'

class ExplosionEvent(SeismicEvent):
    EVENT_TYPE = 'explosion'

class EventManager:
    def __init__(self, events=[]):
        self.events = events

    def add_event(self, event):
        self.events.append(event)

    def max_earthquakes_location(self):
        """Return the location with most earthquakes"""
        locations = [e.locationSource for e in self.events]
        return statistics.mode(locations) if locations else None

    def daily_histogram(self, target_format='%Y-%m-%d', target_tz='UTC'):
        """Return frequency of events for each day"""
        days = defaultdict(int)
        for e in self.events:
            date = convert_datetime(e.time, target_format=target_format,
                                    target_tz=target_tz)
            days[date] += 1

        ordered_dates = OrderedDict(sorted(days.items(), key=lambda dt: dt[0]))
        return ordered_dates

    def average_magnitude_location(self, location):
        """Calculate the average magnitude for a given location"""

        magnitudes = [Decimal(e.mag) for e in list(
            filter(lambda x: x.locationSource == location, self.events))]

        return {location: round(statistics.mean(magnitudes) if magnitudes else 0, 2)}

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
            locs[key]['avg'] = statistics.mean(magnitudes) if magnitudes else 0

        return {key: round(locs[key]['avg'], 2) for key in locs}
