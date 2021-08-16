from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_air():
    visited = [[False] * c for _ in range(r)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    count = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                if board[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append([ny, nx])
                elif board[ny][nx] == 1:
                    board[ny][nx] = 0
                    count += 1
                    visited[ny][nx] = True
    cheese.append(count)
    return count


r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
cheese = []

time = 0
while True:
    time += 1
    count = find_air()
    if count == 0:
        break
print(time - 1)
print(cheese[-2])
