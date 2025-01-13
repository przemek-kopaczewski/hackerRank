from itertools import combinations
n = int(input())
k = list(map(str, input().split()))
c = int(input())

all = 0
a = 0

for komb in combinations(k, c):
    print(komb)
    all += 1
    if 'a' in komb:
        a += 1

print(round(a / all, 3))