def solution(n, times):
    answer = 0
    # 최소 분(left), 최대로 걸릴 수 있는 분(right)
    left, right = 1, max(times) * n
    while left <= right:
        # left보다 right가 크거나 같은 동안 left, right를 이동시키며 가운데 mid로 시간을 탐색.
        people = 0
        # 이분탐색
        mid = (left + right) // 2
        for time in times:
            people += mid // time
            # 심사 받은 사람이 받을 사람 수 보다 많으면 break
            if people >= n:
                break
        # 심사 받은 사람이 받을 사람 수 보다 많거나 같으면 mid를 답으로 하고 답이 같을 때 까지 시간 단축
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
