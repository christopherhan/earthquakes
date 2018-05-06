import unittest
from decimal import Decimal
from earthquake2 import EventManager, EarthquakeEvent

class TestEventManager(unittest.TestCase):
    def setUp(self):

        # TODO use a factory
        events = [
            EarthquakeEvent(time='2018-04-04T20:06:13.737Z', mag='1.5',
                            locationSource='ak', type='earthquake'),
            EarthquakeEvent(time='2018-04-04T20:06:09.925Z', mag='1.3',
                            locationSource='ak', type='earthquake'),
            EarthquakeEvent(time='2018-04-04T19:47:33.010Z', mag='3.07',
                            locationSource='pr', type='earthquake'),
            EarthquakeEvent(time='2018-04-05T19:11:01.660Z', mag='3.1',
                            locationSource='us', type='earthquake')
        ]
        self.hist_data = {'2018-04-04': 3, '2018-04-05': 1}

        self.manager = EventManager(events=events)

    def test_max_earthquakes_location(self):
        """Test getting location with highest earthquakes"""
        loc = self.manager.max_earthquakes_location()
        self.assertEqual(loc, 'ak')

    def test_daily_histogram(self):
        """Test generating daily histogram"""
        hist = self.manager.daily_histogram()
        self.assertEqual(self.hist_data, hist)

    def test_average_magnitude_location(self):
        """Test getting the average magnigude for a location"""
        avg = self.manager.average_magnitude_location('ak')
        self.assertEqual({'ak': Decimal('1.40')}, avg)

        avg2 = self.manager.average_magnitude_location('pr')
        self.assertEqual({'pr': Decimal('3.07')}, avg2)

    def test_average_magnitude_locations(self):
        """Test getting the average magnitude for a single location"""
        locs = self.manager.average_magnitude_locations()
        avgs = {
            'ak': Decimal('1.40'),
            'pr': Decimal('3.07'),
            'us': Decimal('3.10')
        }
        self.assertEqual(locs, avgs)
