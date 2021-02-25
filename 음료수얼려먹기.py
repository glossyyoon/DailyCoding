def dfs(x, y):
    if x<=-1 or y<=-1 or x>a-1 or y>b-1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

a, b = map(int, input().split(" "))
graph = []
result = 0
for i in range(a):
    graph.append(list(input()))

for i in range(a):
    for j in range(b):
        if dfs(i, j) == True:
            result += 1
print(result)