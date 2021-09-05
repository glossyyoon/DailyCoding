import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())


def bfss(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    l = 0
    while q:
        l += 1
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if baechu[nx][ny] == 1:
                    baechu[nx][ny] = 0
                    q.append((nx, ny))


for _ in range(t):
    count = 0
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    baechu = [[0] * m for _ in range(n)]
    for i in range(k):
        y, x = map(int, sys.stdin.readline().rstrip().split())
        baechu[x][y] = 1
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    for i in range(n):
        for j in range(m):
            if baechu[i][j] == 1:
                baechu[i][j] = 0
                bfss(i, j)
                count += 1
    print(count)
