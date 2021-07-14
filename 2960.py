import sys

N, K = map(int, sys.stdin.readline().split())
s = [True] * (N + 1)
count = 0
for i in range(2, N + 1):
    for j in range(i, len(s), i):
        if s[j]:
            s[j] = False
            count += 1
            if count == K:
                print(j)
                break
