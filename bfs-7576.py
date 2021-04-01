from collections import deque
n, m = map(int, input().split())
tomato = []
queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(m):
    tomato.append(list(map(int, input().split())))

count = 0
visited = [[0 for _ in range(n)] for _ in range(m)]
    


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if tomato[nx][ny]==0:
                    tomato[nx][ny] += 1
                    queue.append([nx, ny])
# bfs()
# result = -2
# for i in range(m):
#     for j in range(n):
        
#         result = max(result, j)

# if count == 0:
#     print(-1)
# else:
#     print(result)

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append([i, j])
bfs()
isTrue = False
result = -2
for i in tomato:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)