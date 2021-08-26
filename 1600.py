import sys
from collections import deque

k = int(sys.stdin.readline().rstrip())
w, h = map(int, sys.stdin.readline().rstrip().split())
monkey = []
for _ in range(h):
    monkey.append(list(map(int, sys.stdin.readline().rstrip().split())))
queue = deque()
queue.append((0, 0))

ddx = [-1, -2, -2, -1, 1, 2, 2, 1]
ddy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dist = [[0] * h for _ in range(w)]
while queue:
    x, y = queue.popleft()
    if x == h - 1 and y == w - 1:
        print(dist[x][y])
        break
    if k > 0:
        for i in range(8):
            nx = x + ddx[i]
            ny = y + ddy[i]
            if 0 <= nx < h and 0 <= ny < w:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
                k -= 1
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < h and 0 <= ny < w:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))
if not queue:
    print(-1)
