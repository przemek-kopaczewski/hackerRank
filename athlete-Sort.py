nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

arr = sorted(arr, key=lambda element: element[k])

for row in arr:
    print(" ".join(map(str, row)))