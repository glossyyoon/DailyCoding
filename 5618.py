import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))


def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)


g = GCD(s[0], GCD(s[1], s[-1]))
for i in range(1, g // 2 + 1):
    if g % i == 0:
        print(i)
print(g)
