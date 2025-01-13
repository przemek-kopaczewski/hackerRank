bla = input()
a = set(map(str, input().split()))

for i in range(int(input())):
    action = input().split()
    values = set(map(str, input().split()))
    exec(f'a.{action[0]}({values})')

a = map(int, a)
print(sum(a))