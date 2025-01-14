#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    for number in a:
        if a.count(number) == 1:
            return number




n = int(input().strip())
a = list(map(int, input().rstrip().split()))
print(lonelyinteger(a))
