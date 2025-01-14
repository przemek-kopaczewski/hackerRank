#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    n = bin(n)[2:]
    final_num = '0'*32
    final_num = final_num[:len(final_num)-len(n)]+n
    final_num = final_num.translate(str.maketrans({"0": "1", "1": "0"}))
    return int(final_num, 2)

q = int(input().strip())

for q_itr in range(q):
    n = int(input().strip())
    result = flippingBits(n)
    print(result)
