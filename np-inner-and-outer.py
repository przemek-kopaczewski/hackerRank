import numpy

A = []
B = []

A.append(list(map(int, input().split())))
B.append(list(map(int, input().split())))

A, B = numpy.array(A), numpy.array(B)

inner = numpy.inner(A, B)
print(inner.item())
print(numpy.outer(A, B))
