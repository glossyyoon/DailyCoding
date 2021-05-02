a, b = map(int, input().split())


def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


g = GCD(a, b)
print(g)
print(g * (a // g) * (b // g))
