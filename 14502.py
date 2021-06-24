from collections import deque
import copy
import sys
n, m = map(int, sys.stdin.readline().split())
ans = 0
queue = deque()


def makeWall(x):
    if x == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if center[i][j] == 0:
                center[i][j] = 1
                makeWall(x + 1)
                center[i][j] = 0


def bfs():
    global ans
    w = copy.deepcopy(center)
    for i in range(n):
        for j in range(m):
            if w[i][j] == 2:
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    queue.append([nx, ny])
    counter = 0
    for i in w:
        counter += i.count(0)
    ans = max(ans, counter)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

center = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
counter = 0
max_result = 0
makeWall(0)
print(ans)