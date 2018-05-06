import csv
from earthquake import AverageMagnitude
from earthquake2 import EventManager, EarthquakeEvent, ExplosionEvent
from utils.encoding import print_results


def get_fields(select_fields, fields):
    """Get specific fields and their corresponding index from list of `fields`.

    Args:
        select_fields (:obj:`list` of :obj: `str`): Subset of strings to be
            selected from `fields`
        fields (:obj:`list` of :obj: `str`:): List of all fields
    Returns:
        dict({'time': 0, 'mag': 4, 'type': 14, 'locationSource': 20})

    """
    field_indices = [(field, headings.index(field)) for field in fields]
    filtered = list(filter(lambda x: x[0] in select_fields, field_indices))
    return dict((x, y) for x, y in filtered)

def get_field_values(row, fields, filter_by=None):
    attributes = {}

    # Skip the rows with fields we don't want
    if filter_by:
        filter_field = filter_by[0]
        filter_value = filter_by[1]

        filter_index = fields[filter_field]
        if row[filter_index] != filter_value:
            return None

    for key in fields.keys():
        index = fields[key]
        attributes[key] = row[index]

    return attributes

if __name__ == '__main__':

    DATA_SOURCE = 'data/1.0_month.csv'
    FILTER_BY = ('type', EarthquakeEvent.EVENT_TYPE)

    SELECT_FIELDS = ['time', 'locationSource', 'mag', 'type']

    manager = EventManager()

    with open(DATA_SOURCE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headings = next(reader)

        fields = get_fields(SELECT_FIELDS, headings)

        for row in reader:
            attributes = get_field_values(row, fields, filter_by=FILTER_BY)
            if not attributes:
                continue

            event = EarthquakeEvent(**attributes)
            manager.add_event(event)

            # Question 4 Extra Credit. Simulate callback being invoked
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
    print_results(AverageMagnitude.query('ak'), heading='Question 4 extra credit (Querying "ak")')
