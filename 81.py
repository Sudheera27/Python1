import datetime as dt
import pytz
cities=["US/Pacific","US/Eastern","Europe/London",'Asia/Dubai','Asia/Kolkata','Asia/Singapore','Asia/Tokyo','Australia/Sydney']
times1=[]
len1=len(cities)
for i in range(0,len1,1):
    r1=pytz.timezone(cities[i])
    t1=str(dt.datetime.now(r1))
    times1.append(t1+" "+cities[i])
print(times1)
    
