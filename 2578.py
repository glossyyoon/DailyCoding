import sys

order = []
bingo = [list(map(int, sys.stdin.readline().split())) for i in range(5)]
for i in range(5):
    w = list(map(int, input().split()))
    for j in w:
        order.append(j)
result = 0


def isBingo(bingo):
    count = 0
    for i in range(5):  #가로
        summ = 0
        for j in range(5):
            summ += bingo[i][j]
        if summ == 0:
            count += 1
    for i in range(5):  #세로
        summ = 0
        for j in range(5):
            summ += bingo[j][i]
        if summ == 0:
            count += 1
    summ = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                summ += bingo[i][j]
    if summ == 0:
        count += 1

    summ = 0
    for i in range(5):
        for j in range(5):
            if j == 4 - i:
                summ += bingo[i][j]
    if summ == 0:
        count += 1
    return count


for idx, num in enumerate(order):
    for m in bingo:
        if num in m:
            m[m.index(num)] = 0
            break
    res = isBingo(bingo)
    if res >= 3:
        print(idx + 1)
        break