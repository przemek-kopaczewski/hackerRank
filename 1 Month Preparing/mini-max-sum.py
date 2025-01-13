def miniMaxSum(arr):
    sum_arr = sum(arr)
    min, max = sum_arr - arr[0], sum_arr - arr[0]
    for i in arr:
        if min > sum_arr - i:
            min = sum_arr - i
        elif max < sum_arr - i:
            max = sum_arr - i

    return f'{min} {max}'

arr = list(map(int, input().rstrip().split()))
print(miniMaxSum(arr))
