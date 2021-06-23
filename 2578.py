bingo = [list(map(int, input().split())) for i in range(5)]
nums = [list(map(int, input().split())) for i in range(5)]
check = [[False] * 5 for _ in range(5)]


def erase(num):
    for k in range(5):
        temp = num[k]
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == temp:
                    check[i][j] = True
        isItBingo(bingo)


def isItBingo(check):
    count = 0
    for i in range(5):
        flag = True
        if False in check[i]:
            flag = False
        if flag:
            count += 1
    col = list(map(list, zip(*check)))
    print(col)
    for i in range(5):
        for j in range(5):
            flag = True
            if False in col:
                print(1)


for i in range(5):
    erase(nums[i])
print(bingo)