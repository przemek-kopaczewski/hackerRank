n = int(input().strip())
a = list(map(int, input().rstrip().split()))

swaps = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swaps+=1

print(a)
print(f'Array is sorted in {swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'First Element: {a[-1]}')