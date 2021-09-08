import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
MAX = 200000
check = [False] * (MAX + 1)
check[n] = True
dist = [-1] * (MAX + 1)
dist[n] = 0
queue = deque()
queue.append(n)
while queue:
    now = queue.popleft()
    for idx in [now - 1, now + 1, now * 2]:
        if 0 <= idx <= MAX and not check[idx]:
            check[idx] = True
            dist[idx] = dist[now] + 1
            queue.append(idx)
print(dist[m])
