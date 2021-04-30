from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
computer = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    computer[b].append(a)


def bfs(x):
    count = 0
    queue = deque()
    queue.append(x)
    visited = [0] * (n + 1)
    visited[x] = 1
    while queue:
        v = queue.popleft()
        count += 1
        for i in computer[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
    return count


ans = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    ans[i] = bfs(i)
for j in range(1, n + 1):
    if ans[j] == max(ans):
        print(j, end=' ')