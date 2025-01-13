cube = lambda x: x**3

def fibonacci(n):
    a, b = 0, 1
    stdout = []
    for _ in range(n):
        stdout.append(a)
        a, b = b, a + b
    return stdout

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))