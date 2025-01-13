from itertools import combinations_with_replacement

s, k = map(str, input().split())

list_of_combination = list(combinations_with_replacement(sorted(s), int(k)))

for i in list_of_combination:
    print(''.join(i))
