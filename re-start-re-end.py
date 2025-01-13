import re

string = input()
k = input()
pattern = rf"(?=({k}))"

matches = list(re.finditer(pattern, string))
if len(list(matches)) > 0:
    for match in matches:
        start = match.start()
        end = start + len(k)-1

        span = (start, end)
        print(span)
else:
    print((-1, -1))
