n = int(input())
s = list(map(int, input().split()))


def LCM(a, b):
    if a % b == 0:
        return b
    else:
        r = a % b
        return LCM(b, a % b)


g = LCM(s[0], LCM(s[1], s[-1]))
for i in range(1, g // 2 + 1):
    if g % i == 0:
        print(i)
print(g)
