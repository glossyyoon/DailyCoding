count, nation = map(int, input().split())
arr = [[0, 0, 0, 0, 0, 0]]
for i in range(1, count+1):
    arr.append(list(map(int, input().split())))
    arr[i].append(1)
    arr[i].append(1)
for j in range(1, count+1):
    arr[j][4] = arr[j][1]*5000 + arr[j][2]*50 + arr[j][3]+1
for k in range(1, count+1):
    for m in range(1, count+1):
        if k!= m and arr[k][4]<arr[m][4]:
            arr[k][5]+= 1
for a in range(0, count+1):
    if nation == arr[a][0]:
        print(arr[a][5])