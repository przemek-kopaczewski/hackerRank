import re
pattern = r"^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?!.*(.).*\1)[A-Za-z0-9]{10}$"
for i in range(int(input())):
    string = input()
    if bool(re.match(pattern, string)):
        print('Valid')
    else:
        print('Invalid')