import numpy

numbers = list(map(int, input().split()))

def zeros(numbers):
    zero = numpy.zeros((numbers), dtype=numpy.int32)
    print(zero)

def ones(numbers):
    one = numpy.ones((numbers), dtype=numpy.int32)
    print(one)

zeros(numbers)
ones(numbers)