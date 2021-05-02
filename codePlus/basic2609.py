a, b = map(int, input().split())


def GCD(a, b):
    for i in range(min(a, b)):
        if a == 0 or b == 0:
            # print(max(a, b))
            return max(a, b)
            break
        else:
            a, b = b, a % b


def LCM(a, b, rGCD):
    return (rGCD * (a // rGCD) * (b // rGCD))


print(GCD(a, b))
print(LCM(a, b, GCD(a, b)))