from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
maps = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().rstrip().split())
    maps[r - 1][c - 1] = 1
l = int(input())
direction = []
for _ in range(l):
    x, c = input().rstrip().split()
    direction.append((int(x), c))
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
x, c = direction[0]
tail = deque()
tail.append((0, 0))
i, j = 0, 0
maps[i][j] = -1
idx = 1
time = 0
d = 0
while True:
    if time == x:
        if c == "D":
            d -= 1
            if d == -1:
                d = 3
        else:
            d += 1
            if d == 4:
                d = 0
        if idx < l:
            x, c = direction[idx]
            idx += 1
    newI, newJ = i + dx[d], j + dy[d]
    time += 1
    if 0 <= newI < n and 0 <= newJ < n:
        if maps[newI][newJ] == -1:
            print(time)
            break
        elif maps[newI][newJ] == 0:
            maps[newI][newJ] = -1
            tail.append((newI, newJ))
            p, q = tail.popleft()
            maps[p][q] = 0
        else:
            maps[newI][newJ] = -1
            tail.append((newI, newJ))
        i, j = newI, newJ
    else:
        print(time)
        break
