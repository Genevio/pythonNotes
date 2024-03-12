#date and time func in py

import datetime as dt

cu_date = dt.date.today()
print("current date:", cu_date)

new = dt.date(2024,3,25)
print(new)
print("year :", new.year)
print("month :", new.month)
print("Day :", new.day)

a=dt.time(10,45,5,666656)
print(a)
print("hour:", a.microsecond)

cu_time = dt.datetime.now()
print(cu_time)

new= dt.datetime(2025,5,31,10,2)
print(new)
print(new.date())
print(new.time())

#diff
"""
cu = dt.datetime.now()
new_yr = dt.datetime(2025,1,1)
diff=cu-new_yr
print("""

cu = dt.datetime.now()
print(cu)
s=cu.strftime("%A %b %d %Y")
print(s)

#math
