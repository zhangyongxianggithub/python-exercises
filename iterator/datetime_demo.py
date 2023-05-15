import datetime
import time

print(datetime.datetime(year=2023, month=1, day=1, hour=23, minute=59, second=0))

current_milli_time = lambda: int(round(time.time() * 1000))
print(current_milli_time())
