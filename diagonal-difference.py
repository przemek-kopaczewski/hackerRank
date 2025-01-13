def diagonalDifference(arr):
    sumLeftDiagonal = 0
    sumRightDiagonal = 0
    i = 0
    j = len(arr)-1
    for row in arr:
        sumLeftDiagonal += row[i]
        i+=1
        sumRightDiagonal += row[j]
        j-=1

    return abs(sumLeftDiagonal - sumRightDiagonal)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)