from datetime import datetime
def timeConversion(s):
    time_object = datetime.strptime(s, '%I:%M:%S%p')
    return time_object.strftime("%H:%M:%S")

s = input()
result = timeConversion(s)
print(result)