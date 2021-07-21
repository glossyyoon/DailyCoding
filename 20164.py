from itertools import combinations
import math

n = input()
counts = []
min_c = math.inf
max_c = 0


def f_conduct(n, c):
    n = list(n)
    for i in range(len(n)):
        if int(n[i]) % 2 == 1:
            c += 1
    a = ""
    for i in range(len(n)):
        a += n[i]
    conduct(a, c)


def conduct(n, c):
    global min_c, max_c
    temp = c
    if len(n) == 1:
        min_c = min(min_c, c)
        max_c = max(max_c, c)
    if len(n) == 2:
        a, b = n[0], n[1]
        if (int(a) + int(b)) % 2 == 1:
            c += 1
        return conduct(str(int(a) + int(b)), c)
    else:
        a = list(combinations(range(1, len(n)), 2))
        for i in range(len(a)):
            c = temp
            s1, s2 = a[i][0], a[i][1]
            q = n[:s1]
            p = n[s1:s2]
            r = n[s2:]
            d = str(int(q) + int(p) + int(r))
            for i in range(len(d)):
                if int(d[i]) % 2 == 1:
                    c += 1

            conduct(d, c)


f_conduct(n, 0)
print(min_c, max_c)
