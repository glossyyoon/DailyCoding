#참고
num = int(input())
arr = [0, 1, 1, 2, 3, 5]
for i in range(6, num+1):
    arr.append(arr[i-2]+arr[i-1])
print(arr[num])