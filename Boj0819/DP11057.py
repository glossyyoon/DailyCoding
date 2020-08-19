num = int(input())

arr = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
for i in range(2, num):
    arr.append([0]*10)
    for j in range(0, 10):
        count = 0
        for k in range(j, 10):
            count += arr[i-1][k]
        arr[i][j] = count
result = 0
for p in range(0, 10):
    result += arr[num-1][p]
print(result%10007)