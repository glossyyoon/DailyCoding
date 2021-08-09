import sys
from collections import deque

r, c, n = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(r):
    arr.append(list(sys.stdin.readline().rstrip()))
queue = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def load_bomb():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == ".":
                arr[i][j] = "O"


def location_bomb():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == "O":
                queue.append((i, j))


def explode():
    while queue:
        bomb = queue.popleft()
        x, y = bomb[0], bomb[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                arr[nx][ny] = "."


n -= 1
while n:
    location_bomb()
    load_bomb()
    n -= 1
    if n == 0:
        break
    explode()
    n -= 1

for i in range(r):
    for j in range(c):
        print(arr[i][j], end="")
    print()
