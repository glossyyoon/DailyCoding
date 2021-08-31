import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())  # 세로,가로
road = []
for i in range(n):
    r = list(map(int, sys.stdin.readline().rstrip().split()))
    road.append(r)

queue1 = deque()
destination = []
dist = [[-1] * m for _ in range(n)]


check = [[False] * m for _ in range(n)]


def bfs(queue):
    while queue:
        current = queue.popleft()
        x, y = current[0], current[1]
        check[x][y] = True
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny] and road[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                    check[nx][ny] = True


for i in range(n):
    for j in range(m):
        if road[i][j] == 0:
            dist[i][j] = 0
        elif road[i][j] == 2:
            queue1.append((i, j))
            check[i][j] = True
            dist[i][j] = 0

bfs(queue1)
for i in range(n):
    for j in range(m):
        print(dist[i][j], end=" ")
    print()
