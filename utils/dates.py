from dateutil import parser
from dateutil import tz

def convert_datetime(date_str, target_format='%Y-%m-%d', target_tz=None):
    """
    Converts an ISO8601 formatted string to a target format and optional target timezone.
    """

    d = parser.isoparse(date_str)
    if target_tz:
        utc = d.replace(tzinfo=tz.gettz('UTC'))
        d = utc.astimezone(tz.gettz(target_tz))

    converted = d.strftime(target_format)

    return converted
