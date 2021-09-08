import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
MAX = 200000
check = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)
queue = deque()
queue.append(n)
dist[n] = 0
check[n] = True

via = [-1] * MAX
via.append(n)
while queue:
    now = queue.popleft()
    if now * 2 < MAX and not check[now * 2]:
        queue.appendleft(now * 2)
        check[now * 2] = True
        dist[now * 2] = dist[now] + 1
        via[now * 2] = now
    if now - 1 > 0 and not check[now - 1]:
        queue.append(now - 1)
        check[now - 1] = True
        dist[now - 1] = dist[now] + 1
        via[now - 1] = now
    if now + 1 < MAX and not check[now + 1]:
        queue.append(now + 1)
        check[now + 1] = True
        dist[now + 1] = dist[now] + 1
        via[now + 1] = now
print(dist[k])


def go(n, m):
    if n != m:
        go(n, via[m])
    print(m, end=" ")


go(n, k)
