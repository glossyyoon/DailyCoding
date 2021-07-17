from itertools import combinations

n = input()
counts = []


def conduct(n, count):
    if len(n) == 1:
        counts.append(count)
        return
    if len(n) == 2:
        a, b = n[0], n[1]
        if int(a) % 2 == 1:
            count += 1
        if int(b) % 2 == 1:
            count += 1
    if len(n) >= 3:
        a = list(combinations(range(1, len(n)), 2))
        for i in range(len(a)):
            s1, s2 = a[i][0], a[i][1]
            q = n[:s1]
            p = n[s1:s2]
            r = n[s2:]
            if int(q) % 2 == 1:
                count += 1
            if int(p) % 2 == 1:
                count += 1
            if int(r) % 2 == 1:
                count += 1
            conduct(q, count)
            conduct(p, count)
            conduct(r, count)


conduct(n, 0)
print(counts)
