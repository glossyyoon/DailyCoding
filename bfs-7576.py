n, m = map(int, input().split())
tomato = []
for i in range(m):
    tomato.append(list(map(int, input().split())))
count = 0
   
def bfs(x, y):
    global count
    if x<0 or x>=m or y<0 or y>=n:
        return False
    if tomato[x][y] == -1:
        return False
    if tomato[x][y]==1:
        bfs(x, y+1)
        bfs(x, y-1)
        bfs(x+1, y)
        bfs(x-1, y)
        return True
    if tomato[x][y]==0:
        count += 1
        tomato[x][y] = 1
        bfs(x, y+1)
        bfs(x, y-1)
        bfs(x+1, y)
        bfs(x-1, y)
        return True
    return False

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            if bfs(i, j)==True:
                print(True)
                count += 1
if count == 0:
    print(-1)
else:
    print(count)

