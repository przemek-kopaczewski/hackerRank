def towerBreakers(n, m):
    

t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = towerBreakers(n, m)