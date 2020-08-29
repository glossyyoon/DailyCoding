arr = list(map(int, input()))
result = []
arr.sort()
for i in range(len(arr)-1, -1,  -1):
    result.append(arr[i])
for j in range(len(arr)):
    print(result[j], end = "")