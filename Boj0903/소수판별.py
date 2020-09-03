#에라토스테네스의 체
num = int(input())
arr = []
for i in range(0, num+1):
    arr.append(i)

for i in range(2, num+1):
    for j in range(i+i, num+1, i):
        arr[j] = 0

for i in range(num):
    if arr[i]!=0:
        print(arr[i])
