import numpy as np

N, M, P = map(int, input().split())

arr = []

for i in range(N+M):
    row = list(map(int, input().split()))
    arr.append(row)

arr = np.array(arr)

print(arr)
