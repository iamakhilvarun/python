import datetime
import locale

# locale.setlocale(locale.LC_ALL,'fr_FR.utf-8')  # --> '' uses system default settings
locale.setlocale(locale.LC_ALL, "")

start = datetime.date(2026, 7, 6)  # year-month-day
print(start)

pretty_start = start.strftime("%A %d %B, %Y")  # day - date - month - year
print(pretty_start)


duration = datetime.timedelta(
    days=15, hours=48, seconds=90
)  # creates a datetime diffrence of 15 days , hours are increased
end = start + duration

print(end)
print(duration)

# printing hours , minutes ,seconds seprately
d1 = datetime.timedelta(hours=2)
d2 = datetime.timedelta(minutes=120)
d3 = datetime.timedelta(seconds=7200)

print(d1, d2, d3, sep=", ")
print(repr(d1), repr(d2), repr(d3), sep=",  ")

diffrence = end - start

print(diffrence)
print(diffrence == duration)
