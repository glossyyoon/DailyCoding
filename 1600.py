import sys
from collections import deque

k = int(sys.stdin.readline().rstrip())
w, h = map(int, sys.stdin.readline().rstrip().split())
monkey = []

for _ in range(h):
    monkey.append(list(map(int, sys.stdin.readline().rstrip().split())))

queue = deque()
queue.append((0, 0, k))

ddx = [-2, -1, 1, 2, 2, 1, -1, -2]
ddy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visit = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]


def bfs():
    while queue:
        x, y, z = queue.popleft()
        if x == h - 1 and y == w - 1:
            return visit[x][y][z]
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if (
                0 <= nx < h
                and 0 <= ny < w
                and visit[nx][ny][z] == 0
                and monkey[nx][ny] == 0
            ):
                visit[nx][ny][z] = visit[x][y][z] + 1
                queue.append((nx, ny, z))
        if z > 0:
            for i in range(8):
                nx = x + ddx[i]
                ny = y + ddy[i]
                if (
                    0 <= nx < h
                    and 0 <= ny < w
                    and visit[nx][ny][z - 1] == 0
                    and monkey[nx][ny] == 0
                ):
                    visit[nx][ny][z - 1] = visit[x][y][z] + 1
                    queue.append((nx, ny, z - 1))
    return -1


print(bfs())
# for i in range(h):
#     for j in range(w):
#         print(dist[i][j], end=" ")
#     print()
