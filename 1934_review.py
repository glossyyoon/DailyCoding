T = int(input())
# 유클리드 호제법을 이용한 최대공약수, 최소공배수 구하기


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def lcm(a, b):
    G = gcd(a, b)
    return a * b // G


for i in range(T):
    a, b = map(int, input().split())
    print(lcm(a, b))
