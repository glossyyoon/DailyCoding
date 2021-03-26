def dfs(x, y):
    global count
    if x<0 or x>=num or y<0 or y>=num:
        return False
    if maps[x][y]==1:
        count += 1
        maps[x][y] = 0
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        return True
    return False

num = int(input())
maps = []
counts = []
count = 0
for i in range(num):
    maps.append(list(map(int, input())))
result = 0

for i in range(num):
    for j in range(num):
        if dfs(i, j)==True:
            result += 1
            counts.append(count)
        count = 0
print(result)
counts.sort()
for i in counts:
    print(i)
    