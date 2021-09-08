import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
MAX = 200000
check = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)
check[N] = True
dist[N] = 0
queue = deque()
queue.append(N)
while queue:
    now = queue.popleft()
    check[now] = True
    for idx in [now - 1, now + 1, now * 2]:
        if 0 <= idx <= MAX and not check[idx]:
            check[idx] = True
            dist[idx] = dist[now] + 1
            queue.append(idx)
print(dist[K])
