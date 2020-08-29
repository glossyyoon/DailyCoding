num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
arr.sort()
for j in range(num):
    print(arr[j])