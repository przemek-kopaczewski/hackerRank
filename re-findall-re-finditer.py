import re

string = 'abaabaabaabaae'

pattern = r"(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([AEIOUaeiou]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])"

print(re.findall(pattern, string))

if len(re.findall(pattern, string)) > 0:
    for i in re.findall(pattern, string):
        print(i)
else:
    print(-1)