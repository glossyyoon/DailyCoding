num = int(input())
col = int(input())
arr = []
arr.append([0]*col)
arr.append([0]*col)

element1 = input().split()
element2 = input().split()
for i in range(col):
    arr[0][i] = element1[i]
for j in range(col):
    arr[1][j] = element2[j]
