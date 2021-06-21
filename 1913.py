n = int(input())
k = int(input())
li = [[0 for _ in range(n)] for _ in range(n)]
x = y = n // 2
dx = [-1, 1, 0, 0]  #상하좌우
dy = [0, 0, -1, 1]
count = 1
circle = 0
ans = [0, 0]

while x != 0 and y != 0:
    for i in range(1):

        circle += 1
        if circle != 1:
            count -= 1
        li[x][y] = count
        x += dx[0]
        y += dy[0]
        count += 1
        li[x][y] = count
        if k == count:
            ans[0] = x
            ans[1] = y
        count += 1
    for i in range(circle * 2 - 1):
        x += dx[3]
        y += dy[3]
        li[x][y] = count
        if k == count:
            ans[0] = x
            ans[1] = y
        count += 1
    for i in range(circle * 2):

        x += dx[1]
        y += dy[1]
        li[x][y] = count
        if k == count:
            ans[0] = x
            ans[1] = y
        count += 1
    for i in range(circle * 2):
        x += dx[2]
        y += dy[2]
        li[x][y] = count
        if k == count:
            ans[0] = x
            ans[1] = y
        count += 1
    for i in range(circle * 2):
        x += dx[0]
        y += dy[0]
        li[x][y] = count
        if k == count:
            ans[0] = x
            ans[1] = y
        count += 1

for i in range(n):
    for j in range(n):
        print(li[i][j], end=" ")
    print()
print(ans[0] + 1, end=" ")
print(ans[1] + 1)
