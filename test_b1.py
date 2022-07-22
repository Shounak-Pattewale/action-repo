# New branch created
import datetime, timedelta

dt = datetime.datetime.strptime("2022-07-22T03:56:24+05:30", "%Y-%m-%dT%H:%M:%S%z")
print(dt.date(),dt.time(),type(dt))