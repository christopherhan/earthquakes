import csv
from earthquake import AverageMagnitude
from earthquake2 import EventManager, EarthquakeEvent, ExplosionEvent
from utils.encoding import print_results


def get_field_indices(select_fields, fields):
    """Get specific fields and their corresponding index in `fields`.

    Args:
        select_fields (:obj:`list` of :obj: `str`): Subset of strings to be
            selected from `fields`
        fields (:obj:`list` of :obj: `str`:): List of all fields
    Returns:
        Dictionary whose keys are `select_fields` and values are index in `fields`
    Examples:
        >>> get_fields(['time', 'type'], ['time', 'mag', 'type', 'id'])
        {'time': 0, 'type': 2}

    """
    field_indices = [(field, headings.index(field)) for field in fields]
    filtered = list(filter(lambda x: x[0] in select_fields, field_indices))
    return dict((x, y) for x, y in filtered)

def lookup_field_values(all_fields, select_fields, filter_by=None):
    """
    Look up fields and their values in `all_fields`
    """
    attributes = {}

    # Skip the rows with fields we don't want
    if filter_by:
        filter_field = filter_by[0]
        filter_value = filter_by[1]

        filter_index = fields[filter_field]
        if all_fields[filter_index] != filter_value:
            return None

    for key in fields.keys():
        index = select_fields[key]
        attributes[key] = all_fields[index]

    return attributes

if __name__ == '__main__':

    DATA_SOURCE = 'data/1.0_month.csv'

    # The CSV's field and value we want to filter the data by
    FILTER_BY = ('type', EarthquakeEvent.EVENT_TYPE)

    # A list of CSV fields we want to extract and assign as object attributes
    SELECT_FIELDS = ['time', 'locationSource', 'mag', 'type']

    manager = EventManager()

    with open(DATA_SOURCE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headings = next(reader)

        fields = get_field_indices(SELECT_FIELDS, headings)

        for row in reader:
            attributes = lookup_field_values(row, fields, filter_by=FILTER_BY)
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

    print_results(q1_results, heading='Question 1 Results')
    print_results(q2_results, heading='Question 2 Results')
    print_results(q2_extra_credit, heading=f'Question 2 Extra Credit (America/Los_Angeles)')
    print_results(q3_results, heading='Question 3 Results')
    print_results(q4_results, heading='Question 4 Results')
    print_results(AverageMagnitude.query('ak'), heading='Question 4 extra credit (Querying "ak")')
