import numpy

N = int(input())
arr = []
for rows in range(N):
    numbers = list(map(float, input().split()))
    arr.append(numbers)

print(arr)
print(round(numpy.linalg.det(arr), 2))