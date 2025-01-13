import calendar
from datetime import date
tc = calendar.TextCalendar(firstweekday=0)

data = list(map(int, input().split()))

day, month, year = data[1], data[0], data[2]

print(date(year, month, day).strftime("%A").upper())
