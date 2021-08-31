import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
diff = 100000
check = False
a, b, c = 0, 0, 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if (
                diff >= m - (cards[i] + cards[j] + cards[k])
                and m - (cards[i] + cards[j] + cards[k]) >= 0
            ):
                check = True
                diff = m - (cards[i] + cards[j] + cards[k])
                a, b, c = cards[i], cards[j], cards[k]
if check:
    print(a + b + c)
    print(a, b, c)
