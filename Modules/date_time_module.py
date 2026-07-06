import datetime
import locale

locale.setlocale(locale.LC_ALL,'fr_FR.utf-8')  # --> '' uses system settings 
start = datetime.date(2026, 7, 6)  # year-month-day
print(start)

pretty_start = start.strftime("%A %d %B, %Y")  # day - date - month - year
print(pretty_start)


year = start.year
month=start.month
day=start.day

print(f'The {year} winter olympics started on {day} of the month {month}')


today= datetime.date.today()
print(today)

print(today.strftime('%A'))

print(today.weekday())