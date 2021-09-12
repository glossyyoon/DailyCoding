def solution(N, stages):
    answer = [0] * N
    beyond = [0] * (N + 1)
    fail = [0] * (N + 1)
    for idx, v in enumerate(stages):
        for i in range(1, v):
            beyond[i] += 1
        if v > N:
            fail[N] += 0
        else:
            fail[v] += 1

    for i in range(len(beyond) - 1):
        hap = beyond[i + 1] + fail[i + 1]
        if fail[i + 1] == 0:
            answer[i] = 0
        else:
            answer[i] = fail[i + 1] / hap

    result = {}
    a = []
    for idx, v in enumerate(answer):
        result[idx + 1] = v
    answer = sorted(result, key=lambda x: result[x], reverse=True)
    return answer
