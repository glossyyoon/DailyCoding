def solution(n, left, right):
    answer = [0] * (n * n)
    for i in range(n):
        count = 1 + i
        for j in range(n):
            if i == 0:
                answer[j] = j + 1
            else:
                if j < count:
                    answer[i * n + j] = count
                else:
                    count += 1
                    answer[i * n + j] = count

    return answer[left : right + 1]


print(solution(4, 7, 14))
