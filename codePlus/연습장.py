def solution(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(i, len(arr)):
            if arr[i] == arr[j]:
                count += 1
        arr[i] = count
    for k in arr:
        if k == 0:
            arr.pop(k)
    if arr == []:
        return -1
    else:
        print(arr)


solution([1, 2, 3, 3, 3, 3, 4, 2])