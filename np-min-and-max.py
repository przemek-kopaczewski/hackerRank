import numpy

N, M = map(int, input().split())

arr = []

for rows in range(N):
    numbers = list(map(int, input().split()))
    arr.append(numbers)

arr = numpy.array(arr)
minimum = numpy.min(arr, axis=1)
print(numpy.max(minimum))