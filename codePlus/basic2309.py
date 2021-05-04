import sys
n = 9
a = [int(input()) for _ in range(9)]
a.sort()
for i in range(n):
    for j in range(1, n):
        total = 0
        for k in range(n):
            if i == k or j == k:
                continue
            total += a[k]
        if total == 100:
            for k in range(n):
                if i == k or j == k:
                    continue
                print(a[k])
            sys.exit(0)