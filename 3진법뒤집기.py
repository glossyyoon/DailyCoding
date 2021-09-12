def solution(n):
    answer = ""
    while n >= 1:
        answer += str(n % 3)
        n //= 3

    answer = answer[::-1]
    result = 0
    for idx, v in enumerate(answer):
        result += int(v) * 3 ** (idx)
    return result


print(solution(125))  # 7
