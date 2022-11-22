import datetime
import pytz
from tzwhere import tzwhere


def getLocalTime(lat, lon):
    tz = tzwhere.tzwhere()
    timezone_str = tz.tzNameAt(float(lat), float(lon))
    tzInfo = pytz.timezone(timezone_str)  # localtimezone
    dt = datetime.datetime.now(tz=tzInfo).strftime("%Y-%m-%d %H:%M:%S")

    return dt
