
def get_field_indices(select_fields, fields):
    """Get specific fields and their corresponding index in `fields`.

    Args:
        select_fields (:obj:`list` of :obj: `str`): Subset of strings to be
            selected from `fields`
        fields (:obj:`list` of :obj: `str`:): List of all fields
    Returns:
        Dictionary whose keys are `select_fields` and values are index in `fields`
    Examples:
        >>> get_field_indices(['time', 'type'], ['time', 'mag', 'type', 'id'])
        {'time': 0, 'type': 2}

    """
    field_indices = [(field, fields.index(field)) for field in fields]
    filtered = list(filter(lambda x: x[0] in select_fields, field_indices))
    return dict((x, y) for x, y in filtered)

def lookup_field_values(filter_indices, data, filter_by=None):
    """Look up fields and their values by index in `all_fields`

    Args:
        field_indices ('obj':`dict` of :obj: `int`) Dictionary of fields and
            their indices in data
        data (:obj:`list` of :obj: `str`) List of all fields
        filter_by (:obj:`tuple` of :obj: `str`) Field and value to filter by

    Examples:
        >>> filter_indices = {'time': 0, 'mag': 4, 'type': 5}
        >>> data = ['2018-04-04T19:33:28.420Z', '33.3393333', '-117.143',
        ... '-0.44', '1.08', 'earthquake']
        >>> filter = ('type', 'earthquake')
        >>> lookup_field_values(filter_indices, all_fields, filter_by=filter)
        {'time': '2018-04-04T19:33:28.420Z', 'mag': '1.08', 'type': 'earthquake'}
    """
    field_values = {}

    # Skip the rows with fields we don't want
    if filter_by:
        filter_field = filter_by[0]
        filter_value = filter_by[1]

        filter_index = filter_indices[filter_field]
        if data[filter_index] != filter_value:
            return None

    for key in filter_indices.keys():
        index = filter_indices[key]
        field_values[key] = data[index]

    return field_values
