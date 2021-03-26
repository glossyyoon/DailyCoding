from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        print(queue)
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n - 1][m - 1]


n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
print(bfs(0, 0))
