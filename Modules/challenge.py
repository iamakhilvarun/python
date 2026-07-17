from datetime import datetime, timezone

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

# Timezone names
zones = ("Europe/Paris", "Asia/Kolkata", "Europe/London", "Africa/Nairobi")

# Current UTC time
utc_now = datetime.now(timezone.utc)

for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    required_time = utc_now.astimezone(tz)

    # Get city name
    city = zone.split("/")[-1]

    print(f"The time in {city} is {required_time}")