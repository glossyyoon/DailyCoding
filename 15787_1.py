import sys

n, m = map(int, sys.stdin.readline().split())
train = [0] * n
for _ in range(m):
    op = list(map(int, sys.stdin.readline().split()))
    if op[0] == 1:
        i, x = op[1] - 1, op[2] - 1
        train[i] = train[i] | 1 << x
    for a in range(len(train)):
        print(bin(train[a]))
