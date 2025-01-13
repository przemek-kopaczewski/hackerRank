def lonelyinteger(a):
    for element in a:
        if a.count(element) > 1:
            continue
        else:
            print(element)

n = int(input().strip())

a = list(map(int, input().rstrip().split()))

result = lonelyinteger(a)
