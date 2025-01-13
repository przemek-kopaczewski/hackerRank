a = input()
m = set(map(int, input().split()))
a = input()
n = set(map(int, input().split()))

a = m.difference(n)
b = n.difference(m)

for i in sorted(a.union(b)):
    print(i)