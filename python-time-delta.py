from datetime import datetime

def time_delta(t1, t2):
    t1 = t1[4:]
    t2 = t2[4:]
    t1_math = datetime.strptime(t1, "%d %b %Y %H:%M:%S %z")
    t2_math = datetime.strptime(t2, "%d %b %Y %H:%M:%S %z")
    result = t1_math-t2_math
    print(abs((result.days*24*3600)+(result.seconds)))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
