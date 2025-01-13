def miniMaxSum(arr):
    sumMin = sum(arr) - max(arr)
    sumMax = sum(arr) - min(arr)

    print(str(sumMin) + " " + str(sumMax))


arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)
