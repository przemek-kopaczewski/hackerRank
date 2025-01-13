import numpy

pom = []
N, M = map(int, input().split())
for rows in range(N):
    numbers = list(map(int, input().split()))
    pom.append(numbers)
pom = numpy.array(pom)
print(pom.transpose())
print(pom.flatten())