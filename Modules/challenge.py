from datetime import datetime, timezone

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

# Timezone names
zones = ("Europe/Paris", "Asia/Kolkata", "Europe/London", "Africa/Nairobi")

# Current UTC time
# utc_now = datetime.now(timezone.utc)
local_now = datetime.now()
# replaces the specified parts of a date, time, or datetime object and returns a new object.
local_now = local_now.replace(microsecond=0) 
for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    # required_time = utc_now.astimezone(tz)
    # required_time = datetime.now(tz=tz)
    required_time = local_now.astimezone(tz)
    # Get city name
    city = zone.split("/")[1]

    print(f"The time in {city} is {required_time} {required_time.tzname( )}")
    # print(f"The time in {city} is {required_time.strftime("%m/%d/%Y %H:%M:%S %z %Z")}")
