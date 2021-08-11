import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().rstrip().split())
land = []
queue = deque()
for i in range(n):
    land.append(list(map(int, sys.stdin.readline().rstrip().split())))
day = 0


def calPopulate(x, y):
    queue = deque()
    queue.append([x, y])
    temp = deque()
    temp.append([x, y])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0:
                if l <= abs(land[x][y] - land[nx][ny]) <= r:
                    check[nx][ny] = 1
                    queue.append([nx, ny])
                    temp.append([nx, ny])
    return temp


while True:
    check = [[0] * n for i in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                check[i][j] = 1
                temp = calPopulate(i, j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum(land[x][y] for x, y in temp) // len(temp)
                    for x, y in temp:
                        land[x][y] = num
    if not isTrue:
        break
    day += 1
print(day)
