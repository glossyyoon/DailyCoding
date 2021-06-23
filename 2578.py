bingo = [list(map(int, input().split())) for i in range(5)]
nums = [list(map(int, input().split())) for i in range(5)]

visited = [[False] * 5 for _ in range(5)]
row_visited = [False] * 5
column_visited = [True] * 5
x_visited = [False] * 2  #0:오른쪽 위, 1:오른쪽 아래


def makeBingo():
    for i in range(5):
        if all(visited[i]):
            row_visited[i] = True
    for i in range(5):
        temp = list()
        for j in range(5):
            temp.append(visited[j][i])
        if all(temp):
            column_visited[i] = True

    temp_up = list()
    temp_down = list()

    for i in range(5):
        temp_up.append(visited[i][i])
        temp_down.append(visited[i][4 - i])
    if all(temp_down):
        x_visited[0] = True
        x_visited[1] = True


def countBingo():
    count = 0
    for i in range(5):
        if row_visited[i]:
            count += 1
        if column_visited[i]:
            count += 1
    for i in range(2):
        if x_visited[i]:
            count += 1
    return count


for j in range(len(nums)):
    x = 0
    for i in range(5):
        if nums[j] in bingo[i]:
            x = i
            break

    y = bingo[x].index(nums[j])
    visited[x][y] = True
    makeBingo()
    if countBingo >= 3:
        print(j + 1)
        break