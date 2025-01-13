import re

num = int(input())
text = '\n'.join([input() for i in range(num)])
pattern = r"^(?!#).*"
def andOr(match):
    row = match.group(0)
    if '&&' in row:
        return row.replace('&&', 'and')
    elif '||' in row:
        return row.replace('||', 'or')
    return row


def replace_in_line(match):
    line = match.group(0)
    return re.sub(r"(?<=\s)(&&|\|\|)(?=\s)", andOr, line)


result = re.sub(pattern, replace_in_line, text, flags=re.MULTILINE)
print(result)
