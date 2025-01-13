import numpy

N, M = map(int, input().split())

arr = []

for rows in range(N):
    numbers = list(map(int, input().split()))
    arr.append(numbers)

arr = numpy.array(arr)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr), 11))