import numpy

N, M = map(int, input().split())

l = []

for rows in range(M):
    numbers = list(map(int, input().split()))
    l.append(numbers)


prod = numpy.sum(l, axis=0)

print(numpy.prod(prod))