from decimal import Decimal

class AverageMagnitude:
    locations = {}

    @classmethod
    def callback(cls, data):
        """
        Accepts a row of data from the CSV and calculates a running average
        of the magnitudes per location without storing the sum itself. (Question 4
        extra credit)
        """
        magnitude = data[4].strip()
        location = data[20].strip()

        try:
            loc = cls.locations[location]
            average = loc['average']
            count = loc['count']
        except KeyError:
            loc = cls.locations[location] = {}
            count = loc['count'] = 0
            average = loc['average'] = Decimal('0.00')

        loc['count'] = count+1
        loc['average'] = ((average*count) + Decimal(magnitude)) / (count+1)

    @classmethod
    def query(cls, location):
        """Return the average magnitude for a given location"""
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
