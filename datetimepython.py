import datetime as dt
import time as t
#for handling timezone
import pytz
# date1=dt.date.today()

# print(date1)
# print("Year:",date1.year)
# print("Month:",date1.month)
# print("Day:",date1.day)


# time1=dt.time(12,59,59)

# print(time1)

datetime1=dt.datetime.now()
print(datetime1)

# datetime2=dt.datetime(2012,3,12,3,3,3,3)
# print(datetime2)


# next_ny=dt.datetime(2023,1,1)
# time_rem=next_ny-datetime1
# print(time_rem)
# print(type(time_rem))


timestamp = 1628797222
date_time = dt.datetime.fromtimestamp(timestamp)
print("Date Time using Timestamp:",date_time)
#dtrftime module
time_string=datetime1.strftime("%H:%M:%S")
print("time in Hour:Minute:Second:",time_string)

date_string=datetime1.strftime("%m/%d/%Y, %H:%M:%S")
print("Datetime in mm/dd/yy H:M:S format:",date_string)
#strptime module
date_string="24 November, 2022"
print(date_string)

time_object= dt.datetime.strptime(date_string,"%d %B, %Y")
print(time_object)

#Handling timezone in python
tz_NP=pytz.timezone('Asia/Kathmandu')
datetime_Np =dt.datetime.now(tz_NP)
print("Nepal:",datetime_Np.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London=pytz.timezone('Europe/London')
datetime_London =dt.datetime.now(tz_London)
print("London:",datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

t1=t.localtime()
ct=t.strftime("%H:%M:%S")
print(ct)