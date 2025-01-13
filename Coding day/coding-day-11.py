arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))


total = 0
for rows in range(len(arr)-2):
    for col in range(len(arr)-2):
        a = arr[rows][col]
        b = arr[rows][col+1]
        c = arr[rows][col+2]
        d = arr[rows+1][col+1]
        e = arr[rows+2][col]
        f = arr[rows+2][col+1]
        g = arr[rows+2][col+2]
        if total < sum([a, b, c, d, e ,f ,g]):
            total = sum([a, b, c, d, e ,f ,g])

print(total)
