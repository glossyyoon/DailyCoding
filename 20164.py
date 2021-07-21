from itertools import combinations

n = input()
counts = []


def conduct(n, c):
    if len(n) == 1:
        counts.append(c)
        return
    if len(n) == 2:
        a, b = n[0], n[1]
        if int(a) % 2 == 1:
            c += 1
        if int(b) % 2 == 1:
            c += 1
        return conduct(str(int(a) + int(b)), c)
    if len(n) >= 3:
        a = list(combinations(range(1, len(n)), 2))
        for i in range(len(a)):
            s1, s2 = a[i][0], a[i][1]
            q = n[:s1]
            p = n[s1:s2]
            r = n[s2:]
            d = str(int(q) + int(p) + int(r))
            for i in range(len(d)):
                if int(d[i]) % 2 == 0:
                    c += 1
            conduct(d, c)


conduct(n, 0)
print(counts)
