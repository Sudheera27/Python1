import datetime as dt
import pytz
zones=pytz.all_timezones
#print(zones)
r1=pytz.timezone("US/Pacific")
time1=dt.datetime.now(r1)
print(time1)
