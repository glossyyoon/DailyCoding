n, m = map(int, input().split())


def LCM(a, b, r):
    return a * b // r


def GCD(a, b):
    if a % b == 0:
        return LCM(n, m, b)
    else:
        return GCD(b, a % b)


print(GCD(6, 15))
