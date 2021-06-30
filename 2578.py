import sys

bingo = [list(map(int, sys.stdin.readline().split())) for i in range(5)]
order = [list(map(int, sys.stdin.readline().split())) for i in range(5)]
count = 0
result = 0


def isBingo(bingo):
    global count
    for i in range(5):
        for j in range(5):
            if bingo[i][j]:
                break
            elif all(not bingo[i][j]):  #가로
                count += 1
                print("bingo count+1", bingo)
                break
            elif j == 4:  #세로
                count += 1
                print("bingo count+2", bingo)
                break
            elif i == j and i == 4:  #오른쪽아래 대각선
                count += 1
                print("bingo count+3", bingo)
                break
            elif j == 4 - 1 and i == 4:
                count += 1
                print("bingo count+4", bingo)
                break


def findNum(n):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == n:
                bingo[i][j] = 0
                break


for i in range(5):
    for j in range(5):
        num = order[i][j]
        findNum(num)
        result += 1
        isBingo(bingo)
        if count == 3:
            print(result)
            print(bingo)
            sys.exit()
