def solution(n, lost, reserve):
    answer = 0
    arr = [1] * (n + 1)
    for i in reserve:
        arr[i] += 1
    for i in lost:
        arr[i] -= 1
    for i in range(1, len(arr)):
        if arr[i] == 0 and arr[i - 1] > 1:
            arr[i - 1] -= 1
            arr[i] += 1
        elif arr[i] == 0 and i < len(arr) - 1:
            if arr[i + 1] > 1:
                arr[i + 1] -= 1
                arr[i] += 1
    for k in range(1, len(arr)):
        if arr[k]:
            answer += 1
    return answer
