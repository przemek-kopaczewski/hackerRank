n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

print(' '.join(map(str, arr[::-1])))