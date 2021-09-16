def solution(arr):
    answer = [arr[0]]
    past = arr[0]
    for i in range(len(arr)):
        if past == arr[i]:
            continue
        answer.append(arr[i])
        past = arr[i]

    return answer
