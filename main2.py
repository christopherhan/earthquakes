import csv
from earthquake import AverageMagnitude
from earthquake2 import EventManager, EarthquakeEvent
from utils.encoding import print_results


def get_filtered_fields(select_fields, fields):
    """Get specific fields from list of fields"""
    field_indices = [(field, headings.index(field)) for field in fields]
    filtered = list(filter(lambda x: x[0] in select_fields, field_indices))
    return dict((x, y) for x, y in filtered)


if __name__ == '__main__':

    DATA_SOURCE = 'data/1.0_month.csv'

    FILTER_FIELD = 'type'
    FILTER_VALUE = 'earthquake'

    SELECT_FIELDS = ['time', 'locationSource', 'mag', 'type']

    manager = EventManager()

    with open(DATA_SOURCE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headings = next(reader)

        filtered = get_filtered_fields(SELECT_FIELDS, headings)

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

            # Simulate callback being invoked for Question 4 extra credit
            AverageMagnitude.callback(row)

    question1_results = manager.max_earthquakes_location()
    question2_results = manager.daily_histogram()
    question2_extra_credit = manager.daily_histogram(target_tz='America/Los_Angeles')
    question3_results = manager.average_magnitude_locations()
    question4_results = manager.average_magnitude_location('ci')

    print_results(question1_results, heading='Question 1 Results')
    print_results(question2_results, heading='Question 2 Results')
    print_results(question2_extra_credit, heading=f'Question 2 Extra Credit (America/Los_Angeles)')
    print_results(question3_results, heading='Question 3 Results')
    print_results(question4_results, heading='Question 4 Results')
    print_results(AverageMagnitude.query('ak'), heading='Question 4 extra credit')
