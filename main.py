import datetime
import time
#print(time.time())
print(time.asctime(time.localtime(time.time())))

datetime_object = datetime.datetime.now()
print("Year: ",datetime_object.year)
print("Month: ",datetime_object.month)
print("Day: ",datetime_object.day)
print("Hour: ",datetime_object.hour)
