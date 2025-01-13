input()
numbers = list(map(int, input().split()))

if all(n > 0 for n in numbers) and any(str(n) == str(n)[::-1] for n in numbers):
    print(True)
else:
    print(False)