def plusMinus(arr):
    plus = [x for x in arr if x > 0]
    minus = [x for x in arr if x < 0]
    zero = [x for x in arr if x == 0]

    return f'{len(plus)/len(arr):.6f}\n{len(minus)/len(arr):.6f}\n{len(zero)/len(arr):.6f}'

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(plusMinus(arr))
