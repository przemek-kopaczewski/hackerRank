import numpy as np

N, M = map(int, input().split())
arr = []
for i in range(N*2):
    numbers = list(map(int, input().split()))
    arr.append(numbers)

arr = np.array(arr)
print(np.add(arr[:N], arr[N:]))
print(np.subtract(arr[:N], arr[N:]))
print(np.multiply(arr[:N], arr[N:]))
print(arr[:N] // arr[N:])
print(np.mod(arr[:N], arr[N:]))
print(np.power(arr[:N], arr[N:]))