def GCD(n, m):
    if n % m == 0:
        return m
    else:
        return GCD(m, n % m)


def LCM(n, m, r):
    return n * m // r


def solution(n, m):
    answer = []
    a = GCD(n, m)
    answer.append(a)
    answer.append(LCM(n, m, a))
    return answer


print(solution(3, 12))
