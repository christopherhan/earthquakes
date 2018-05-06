
def get_column_indices(find_columns, headings):
    """Find the column index in a list of headings.

    Args:
        find_columns (:obj:`list` of :obj: `str`): List of column names we want
            to find in list of headings
        headings (:obj:`list` of :obj: `str`:): List of all headings
    Returns:
        Dictionary whose keys are the column name and value is the index
    Examples:
        >>> get_column_indices(['time', 'type'], ['time', 'mag', 'type', 'id'])
        {'time': 0, 'type': 2}
    """
    column_indices = [(field.strip(), headings.index(field)) for field in headings]
    filtered = list(filter(lambda x: x[0] in find_columns, column_indices))
    return dict((col, index) for col, index in filtered)

def lookup_column_values(column_indices, row, filter_by=None):
    """Lookup column values in a row by its index.

    Args:
        column_indices ('obj':`dict` of :obj: `int`) Dictionary of columns and
            their indices in data
        row (:obj:`list` of :obj: `str`) List of all fields
        filter_by (:obj:`tuple` of :obj: `str`) Field and value to filter by

    Returns:
        Dictionary containing the column name and its value in row.
        If `filter_by` is specified, only look for those values. Return None
        in other cases.

    Examples:
        >>> column_indices = {'time': 0, 'mag': 4, 'type': 5}
        >>> row = ['2018-04-04T19:33:28.420Z', '33.3393333', '-117.143',
        ... '-0.44', '1.08', 'earthquake']
        >>> filter = ('type', 'earthquake')
        >>> lookup_column_values(column_indices, row, filter_by=filter)
        {'time': '2018-04-04T19:33:28.420Z', 'mag': '1.08', 'type': 'earthquake'}
    """
    column_values = {}

    if filter_by:
        filter_field, filter_value = filter_by
        filter_index = column_indices[filter_field]

        if row[filter_index] != filter_value:
            return None

    for key in column_indices.keys():
        index = column_indices[key]
        column_values[key] = row[index]

    return column_values
