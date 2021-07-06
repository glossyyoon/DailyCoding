import sys

N, M, R = map(int, sys.stdin.readline().split())
arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

copyArr = [item[:] for item in arr]

boxWidth = M // 2
boxHeight = N // 2

for k in range(R):  #count = 0, 1, 2
    count = boxHeight
    boxW = M - count * 2  #7, 5, 3
    boxH = N - count * 2
    copyArr = [item[:] for item in arr]
    for i in range(count, count + boxH):
        for j in range(count, count + boxW):
            if i == count and j > count:  #상
                arr[i][j - 1] = copyArr[i][j]

            elif i == count + boxH - 1 and j < count + boxW - 1:  #하
                arr[i][j + 1] = copyArr[i][j]

            elif j == count and i < count + boxH - 1:  #좌
                arr[i + 1][j] = copyArr[i][j]

            elif j == count + boxW - 1 and i != count + boxH:  #우
                arr[i - 1][j] = copyArr[i][j]

# while R != 0:
#     for i in range(boxHeight):
# rotating(i)  #꼭짓점 0,0 1,1 2,2
# copyArr = [item[:] for item in arr]
# R -= 1

for i in arr:
    for j in i:
        print(j, end=" ")
    print()
