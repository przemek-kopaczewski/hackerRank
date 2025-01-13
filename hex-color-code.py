import re
pattern = r"[:\s]#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})"
stdout = []
for i in range(int(input())):
    string = input()
    try:
        stdout.append(re.findall(pattern, string))
    except:
        pass

stdout = [x for x in stdout if x != []]
pattern2 = r"#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})"
ex = []

for i in stdout:
    ex.append(re.findall(pattern2, '\n'.join(i)))

stdout = [x for x in ex if x != []]

for i in stdout:
    print('\n'.join(i))
