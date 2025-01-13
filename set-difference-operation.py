bla = input()
a = set(map(str, input().split()))
bla = input()
b = set(map(str, input().split()))

print(len(a.difference(b)))