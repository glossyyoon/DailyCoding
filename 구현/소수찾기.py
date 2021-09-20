import math


def solution(n):
    answer = -1
    arr = [i for i in range(n + 1)]
    idx = 0
    for i in range(2, len(arr)):
        for j in range(i + i, n + 1, i):
            arr[j] = 0
    for i in range(n + 1):
        if arr[i] != 0:
            answer += 1
    return answer


print(solution(10))
