import numpy

numbers = list(map(int, input().split()))
change_array = numpy.array(numbers)
change_array.shape = (3, 3)
print(change_array)