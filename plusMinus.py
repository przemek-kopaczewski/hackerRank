def plusMinus(arr):
    denominator = len(arr)
    plusNum = len([x for x in arr if x > 0])
    zeroNum = len([x == 0 for x in arr if x == 0])
    minusNum = len([x < 0 for x in arr if x < 0])
    print(f"{plusNum/denominator:.6f}\n{minusNum/denominator:.6f}\n{zeroNum/denominator:.6f}")

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr)