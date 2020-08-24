num = int(input())
for i in range(num):
    col = int(input())
    arr = []
    arr.append([0]*col)
    arr.append([0]*col)
    result1 = 0
    result2 = 0
    element1 = input().split()
    element2 = input().split()
    for i in range(col):
        arr[0][i] = int(element1[i])
    for j in range(col):
        arr[1][j] = int(element2[j])
    arr[0][1]+= arr[1][0]
    arr[1][1]+= arr[0][0]
    for k in range(2, col):
        arr[0][k] += max(arr[1][k-1], arr[1][k-2])
        arr[1][k] += max(arr[0][k-1], arr[0][k-2])
    print(max(arr[0][col-1], arr[1][col-1]))