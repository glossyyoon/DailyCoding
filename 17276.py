import sys


def rotate(n, d, arr):
    if d > 0:
        d = abs(d) // 45
        for q in range(d):
            prev_list = []
            for i in range(n):  # 주대각선 저장
                prev_list.append(arr[i][i])
            for i in range(n):  # 주대각선 -> 가운데 열
                prev_temp = arr[i][(n - 1) // 2]
                arr[i][(n - 1) // 2] = prev_list[i]
                prev_list[i] = prev_temp
            for i in range(n):  # 가운데 열 -> 부대각선
                prev_temp = arr[i][n - 1 - i]
                arr[i][n - 1 - i] = prev_list[i]
                prev_list[i] = prev_temp
            for i in range(n):  # 부대각선 -> 가운데 행
                prev_temp = arr[(n - 1) // 2][n - 1 - i]
                arr[(n - 1) // 2][n - 1 - i] = prev_list[i]
                prev_list[i] = prev_temp
            for i in range(n):  # 가운데 행 -> 주대각선
                arr[n - 1 - i][n - 1 - i] = prev_list[i]
    if d < 0:
        d = abs(d) // 45
        for q in range(d):
            prev_list = []
            for i in range(n):  # 주대각선 저장
                prev_list.append(arr[i][i])
            for i in range(n):  # 주대각선 -> 가운데 행
                prev_temp = arr[(n - 1) // 2][i]
                arr[(n - 1) // 2][i] = prev_list[i]
                prev_list[i] = prev_temp
            for i in range(n):  # 가운데 행 -> 부대각선
                prev_temp = arr[n - 1 - i][i]
                arr[n - 1 - i][i] = prev_list[i]
                prev_list[i] = prev_temp
            for i in range(n):  # 부대각선 -> 가운데 열
                prev_temp = arr[n - 1 - i][(n - 1) // 2]
                arr[n - 1 - i][(n - 1) // 2] = prev_list[i]
                prev_list[i] = prev_temp
            for i in range(n):  # 가운데 열 -> 주대각선
                arr[n - 1 - i][n - 1 - i] = prev_list[i]


t = int(sys.stdin.readline())
for i in range(t):
    n, d = map(int, sys.stdin.readline().split())
    arr = []
    for j in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    rotate(n, d, arr)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
