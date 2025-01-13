def countingSort(arr):
    result = [0] * 100

    for num in arr:
        result[num] += 1

    return result

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = countingSort(arr)
print(' '.join(str(element) for element in result))