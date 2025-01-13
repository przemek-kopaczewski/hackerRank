import re

string = "__init__"

pattern = r"([a-zA-Z0-9])\1+"

try:
    print(re.search(pattern, string).group()[0])
except:
    print(-1)