import email.utils
import re

pattern = r"^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z]*\.[a-zA-Z]{1,3}$"

for i in range(int(input())):
    em = input()
    valid = email.utils.parseaddr(em)

    if bool(re.match(pattern, valid[1])):
        valid = email.utils.parseaddr(em)
        print(valid[0] + ' <' + valid[1]+'>')