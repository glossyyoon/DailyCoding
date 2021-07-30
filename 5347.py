import sys

n = int(sys.stdin.readline())


def LCM(n, m, r):
    return n * m // r


def GCD(n, m, a, b):
    if a % b == 0:
        return LCM(n, m, b)
    else:
        return GCD(n, m, b, a % b)


for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    print(GCD(n, m, n, m))
