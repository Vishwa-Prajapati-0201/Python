# Write a Pandas program to create
# a) Date time object for Jan 15 2012.
# b) Specific date and time of 9:20 pm.
# c) Local date and time.
# d) A date without time.
# e) Current date.
# t) Time from a date time.
# g) Current local time.

import pandas as pd
from datetime import datetime, date, time

# a) Date time object for Jan 15, 2012
data1 = pd.Timestamp('2012-01-15')
print("a) Date time object for Jan 15, 2012:", data1)

# b) Specific date and time of 9:20 PM
data2 = pd.Timestamp('2012-01-15 21:20:00')
print("b) Specific date and time of 9:20 PM:", data2)

# c) Local date and time
data3 = pd.Timestamp.now()
print("c) Local date and time:", data3)

# d) A date without time
data4 = pd.Timestamp('2025-04-10').date()
print("d) A date without time:", data4)

# e) Current date
data5 = date.today()
print("e) Current date:", data5)

# f) Time from a datetime
current_datetime = datetime.now()
data6 = current_datetime.time()
print("f) Time from a datetime:", data6)

# g) Current local time
local_time = datetime.now().time()
print("g) Current local time:", local_time)