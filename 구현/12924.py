def solution(n):
    answer = 0
    for num in range(1, n + 1):
        sum = num
        print(num)
        while sum <= n:
            if sum == n:
                answer += 1
                break
            else:
                num += 1
                sum += num
    return answer
