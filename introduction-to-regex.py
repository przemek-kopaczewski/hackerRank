import re
pattern = r"^[+-]?\d*\.\d+$"
stdout = []
for i in range(int(input())):
    if re.match(pattern, input()):
        stdout.append(True)
    else:
        stdout.append(False)

for i in stdout:
    print(i)