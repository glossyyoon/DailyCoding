def dfs(index, numbers, target, value):
    global answer
    if index == len(numbers) and target == value:
        answer += 1
        return
    if index == len(numbers):
        return
    dfs(index + 1, numbers, target, value + numbers[index])
    dfs(index + 1, numbers, target, value - numbers[index])


def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers, target, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
