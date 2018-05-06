from dateutil import parser, tz

def convert_datetime(date_str, from_tz='UTC', target_format=None, target_tz=None):
    """
    Converts an ISO8601 formatted string to an optional target format and
    optional target timezone.
    """

    d = parser.isoparse(date_str)

    if target_tz:
        utc = d.replace(tzinfo=tz.gettz(from_tz))
        d = utc.astimezone(tz.gettz(target_tz))

    if target_format:
        converted = d.strftime(target_format)
    else:
        converted = d.isoformat()

    return converted
