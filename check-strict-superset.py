A = set(map(str, input().split()))

val = 0
value = int(input())

for i in range(value):
    B = set(map(str, input().split()))
    if A.intersection(B) != {}:
        if sorted(A.intersection(B)) == sorted(B):
            val +=1

if val == value:
    print(True)
else:
    print(False)