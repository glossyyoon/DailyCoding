def solution(s, n):
    answer = ""
    print(ord("z"))
    print(ord("Z"))
    for i in s:
        if i == " ":
            answer += " "
            continue
        if ord(i) > 96:
            if ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        else:
            if ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
    return answer


print(solution("a B z", 4))
