from itertools import groupby
string = input().strip()
lista = [list(g) for k, g in groupby(string)]
exit_value = []

for i in lista:
    exit_value.append((len(i), int(i[0])))

[print(i, end=' ') for i in exit_value]