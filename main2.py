import csv
from earthquake import AverageMagnitude
from earthquake2 import EventManager, EarthquakeEvent
from utils.encoding import print_results
from utils.helpers import get_column_indices, lookup_column_values

if __name__ == '__main__':

    DATA_SOURCE = 'data/1.0_month.csv'

    # The CSV field we want to filter the data by. Currently set to filter
    # on the 'type' field and only processes 'earthquake' events.
    FILTER_BY = ('type', EarthquakeEvent.EVENT_TYPE)

    # A list of CSV fields we want to extract and assign as object attributes
    SELECT_FIELDS = ['time', 'locationSource', 'mag', 'type']

    manager = EventManager()

    with open(DATA_SOURCE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headings = next(reader)

        column_indices = get_column_indices(SELECT_FIELDS, headings)

        for row in reader:
            attributes = lookup_column_values(column_indices, row, filter_by=FILTER_BY)
            if not attributes:
                continue

            event = EarthquakeEvent(**attributes)
            manager.add_event(event)

            # Question 4 Extra Credit. Simulate callback being invoked
            AverageMagnitude.callback(row)


    q1_results = manager.max_earthquakes_location()
    q2_results = manager.daily_histogram()
    q2_extra_credit = manager.daily_histogram(target_tz='America/Los_Angeles')
    q3_results = manager.average_magnitude_locations()
    q4_results = manager.average_magnitude_location('ci')
    q4_extra_credit = AverageMagnitude.query('ak')

    print_results(q1_results, heading='Question 1 Results')
    print_results(q2_results, heading='Question 2 Results')
    print_results(q2_extra_credit, heading=f'Question 2 Extra Credit (America/Los_Angeles)')
    print_results(q3_results, heading='Question 3 Results')
    print_results(q4_results, heading='Question 4 Results')
    print_results(q4_extra_credit, heading='Question 4 extra credit (Querying "ak")')
