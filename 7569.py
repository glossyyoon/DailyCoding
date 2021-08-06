import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().rstrip().split())  # m:가로, n:세로
queue = deque()
box = []
dx = [0, 0, -1, 1, 0, 0]  # 상하좌우
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]  # 위아래
for i in range(h):
    arr = []
    for j in range(n):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    box.append(arr)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))
while queue:
    tomato = queue.popleft()
    x, y, z = tomato[2], tomato[1], tomato[0]
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = box[z][y][x] + 1
            queue.append((nz, ny, nx))
maxx = 0
for i in box:
    for j in i:
        for k in j:
            if maxx < k:
                maxx = k
            if k == 0:
                print(-1)
                sys.exit(0)
print(maxx - 1)
