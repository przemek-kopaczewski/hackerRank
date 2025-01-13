from collections import Counter

k = input().split()

for key, value in dict(Counter(k)).items():
    if value == 1:
        print(key)
