import re
pattern = r"^[789][0-9]{9}"

for i in range(int(input())):
    if bool(re.match(pattern, input())):
        print('YES')
    else:
        print('NO')