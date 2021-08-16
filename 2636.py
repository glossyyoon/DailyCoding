import sys
from collections import deque

height, width = map(int, sys.stdin.readline().rstrip().split())
cheeze = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(height)]

# 1이면 가장자리, queue에 넣지 않고 2로 바꿈
# 2이면 한 시간이 지났다고 생각하고 0으로 바꿈
# 0이면 queue에 넣음


def sol():
    visited = [[False] * width for _ in range(height)]
    visited[0][0] = True
    queue = deque()
    queue.append((0, 0))
    count = 0
    while queue:
        x, y = queue.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny]:
                if cheeze[nx][ny] == 1:
                    visited[nx][ny] = True
                    cheeze[nx][ny] = 0
                    count += 1
                elif cheeze[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    arr.append(count)
    return count


arr = []

time = 0
while True:
    time += 1
    c = sol()
    if c == 0:
        break
print(time - 1)
print(arr[-2])
