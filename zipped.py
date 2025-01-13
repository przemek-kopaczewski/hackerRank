n, x = map(int, input().split())
tab = [list(map(float, input().split())) for x in range(x)]
tab = list(zip(*tab))

for i in tab:
    print(sum(i)/len(i))