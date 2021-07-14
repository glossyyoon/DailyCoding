import sys

num = int(sys.stdin.readline())

# 유클리드 호제법
def lcm(a, b):
    r = gcd(a, b)
    return a * b // r


def gcd(a, b):
    return gcd(b % a, a) if b % a else a


for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))
