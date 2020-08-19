num = int(input())
result = 0
arr = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0]
    ]
for i in range(2, num+2):
    arr.append([0]*12)
    for j in range(1, 11):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
for k in range(0, 12):
    result += arr[num-1][k]
print(result%1000000000)