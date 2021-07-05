import sys

L, R = sys.stdin.readline().split()
word = list(sys.stdin.readline())
leftKey = ['qwert', 'asdfg', 'zxcv']
rightKey = ['yuiop', 'hjkl', 'bnm']
count = 0
xl, yl, xr, yr = None, None, None, None
for i in range(3):
    if L in leftKey[i]:
        xl = i
        yl = leftKey[i].index(L)
    if R in rightKey[i]:
        xr = i
        yr = rightKey[i].index(R)

for i in word:
    nextWord = i
    count += 1
    for j in range(3):
        if nextWord in leftKey[j]:
            nx = j
            ny = leftKey[j].index(nextWord)
            count += abs(xl - nx) + abs(yl - ny)
            xl = nx
            yl = ny
            break
        elif nextWord in rightKey[j]:
            nx = j
            ny = rightKey[j].index(nextWord)
            count += abs(xr - nx) + abs(yr - ny)
            xr = nx
            yr = ny
            break

print(count)
