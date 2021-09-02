import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().rstrip().split())  # 세로,가로,제한시간
queue = deque()
maze = []
for i in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip().split())))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            loc = [i, j]
            break


def bfs(queue, maze):
    queue.append((0, 0))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 0
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return dist[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maze[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return -1


def sword(queue, maze):
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 0
    while queue:
        curr = queue.popleft()
        x, y = curr[0], curr[1]
        if x == loc[0] and y == loc[1]:
            maze = [[0] * m for _ in range(n)]
            queue = deque()
            queue.append((x, y))
            x, y = queue.popleft()
            visited[x][[y]] = True
        if x == n - 1 and y == m - 1:
            return dist[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maze[nx][ny] == 0 or maze[nx][ny] == 2:
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return -1


b = bfs(queue, maze)
s = sword(queue, maze)
if b == -1 and s == -1:
    print("Fail")
    sys.exit()
else:
    if b == -1:
        b = 10000
    elif s == -1:
        s = 10000
if b <= t or s <= t:
    print(min(b, s))
else:
    print("Fail")
