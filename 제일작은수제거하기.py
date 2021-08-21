def solution(arr):
    arr.pop(arr.index(min(arr)))
    answer = arr
    if not answer:
        return [-1]
    return answer
