import sys
from collections import deque


def bfs():
    dx = [0, 0, 0, -1, 1, -1, 1, 1, -1]
    dy = [0, -1, 1, 0, 0, 1, 1, -1, -1]
    while queue:
        visit = [[False] * 8 for _ in range(8)]
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == 0 and y == 7:
                return 1

            if wall[x][y] == "#":
                continue

            for k in range(9):
                nx = x + dx[k]
                ny = y + dy[k]
                if (
                    0 <= nx < 8
                    and 0 <= ny < 8
                    and not visit[nx][ny]
                    and wall[nx][ny] == "."
                ):
                    queue.append((nx, ny))
                    visit[nx][ny] = True

        wall.pop()
        wall.insert(0, [".", ".", ".", ".", ".", ".", ".", "."])

    return 0


wall = [list(sys.stdin.readline().rstrip()) for i in range(8)]
queue = deque()
visit = [[False] * 8 for _ in range(8)]
queue.append((7, 0))
# visit[7][0] = True
print(bfs())
