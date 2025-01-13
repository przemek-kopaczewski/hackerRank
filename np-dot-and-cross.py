import numpy

N = int(input())

A = []
B = []

for rows in range(N):
    numbers = list(map(int, input().split()))
    A.append(numbers)

for rows in range(N):
    numbers = list(map(int, input().split()))
    B.append(numbers)

A, B = numpy.array(A), numpy.array(B)

print(numpy.dot(A, B))
