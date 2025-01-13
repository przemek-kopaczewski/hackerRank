import numpy
numpy.set_printoptions(legacy='1.13')

numbers = list(map(float, input().split()))

print(numpy.floor(numbers))
print(numpy.ceil(numbers))
print(numpy.rint(numbers))