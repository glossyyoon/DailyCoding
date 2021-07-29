import sys

n, m = map(int, sys.stdin.readline().split())
N_list = [sys.stdin.readline().strip() for i in range(n)]
M_list = [sys.stdin.readline().strip() for i in range(m)]
d = list(set(N_list) & set(M_list))
print(len(d))
d = sorted(d)
for i in d:
    print(i)
