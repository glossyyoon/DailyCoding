num = int(input())
arr = [0, 1, 2]
for i in range(3, 1001):
    arr.append(arr[i-1]+arr[i-2])
print(arr[num]%10007)