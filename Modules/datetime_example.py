from datetime import time, date

meeting = time(hour=11, minute=15, second=0)
print(meeting)

end_time=time(hour=12,minute=30)
print(end_time)

# print(end_time-meeting) # we cant do it
iso_time='11:15:00'
_time=time.fromisoformat(iso_time)
print(_time)