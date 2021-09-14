def solution(d, budget):
    answer = 0
    d.sort()
    for idx, v in enumerate(d):
        if budget >= v:
            budget -= v
            answer += 1
    return answer


print(solution([1, 3, 2, 5, 4], 9))
