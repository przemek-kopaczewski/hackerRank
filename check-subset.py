for i in range(int(input())):
    input()
    A = set(map(str, input().split()))
    input()
    B = set(map(str, input().split()))
    if sorted(A) == sorted(B.intersection(A)):
        print(True)
    else:
        print(False)
