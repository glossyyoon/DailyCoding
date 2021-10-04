def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        ans = ""
        answer = len(s)
        count = 1
        tempStr = s[:i]  # 앞부분부터 자른 문자

        for j in range(i, len(s), i):
            if tempStr == s[j : i + j]:
                count += 1
            else:
                if count == 1:
                    ans += tempStr
                else:
                    ans += str(count) + tempStr
                tempStr = s[j : i + j]
                count = 1
        if count == 1:
            ans += tempStr
        else:
            ans += str(count) + tempStr
        result.append(len(ans))

    return min(result)
