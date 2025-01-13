import re
n = str(bin(int(input().strip())))

pattern = r"1+"
print(len(max(re.findall(pattern, n), key=len)))
