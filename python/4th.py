#write a program to display current date and time 

import datetime
current=datetime.datetime.now()
print("year",current.year)
print("month",current.month)
print("day",current.day)
print("hour",current.hour)
print("minute",current.minute)
print("second",current.second)