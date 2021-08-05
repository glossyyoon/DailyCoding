import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
check = [[False] * m] * n
queue = deque()
queue.append((0, 0))
count = 1
dx = [0, 0, -1, 1]  # 상하좌우
dy = [-1, 1, 0, 0]
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))
n -= 1
m -= 1

while queue:
    now = queue.popleft()
    x, y = now[0], now[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n and 0 <= ny <= m:
            if arr[nx][ny] == 1:
                count += 1
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
print(arr[n][m])
