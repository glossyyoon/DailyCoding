import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())
box = []
check = []
for i in range(n):
    arr = []
    for j in range(m):
        arr.append(False)
    check.append(arr)
queue = deque()
dx = [0, 0, -1, 1]  # 상하좌우
dy = [-1, 1, 0, 0]
checkDay = 0
for i in range(n):
    box.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(m):
    for j in range(n):
        if box[j][i] == 1:
            # checkDay += 1
            queue.append((j, i))
            check[j][i] = True
if checkDay == m * n:
    print(0)
    sys.exit(0)
count = 0
while queue:
    tomato = queue.popleft()
    x, y = tomato[0], tomato[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0 and not check[nx][ny]:
                # box[nx][ny] = box[x][y] + 1
                box[nx][ny] = 1
                check[nx][ny] = True
                count += 1
                queue.append((nx, ny))
maxx = 0
print(count)
print(box)
for i in box:
    for j in i:
        if maxx < j:
            maxx = j
        if j == 0:
            print(-1)
            sys.exit(0)
# print(maxx - 1)
print(count)
