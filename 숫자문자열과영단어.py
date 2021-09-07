def solution(s):
    answer = ""
    eng = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, v in enumerate(s):
        if v in eng:
            s = s.replace(v, eng[idx])
        answer = s
    return int(s)


print(solution("2three45sixseven"))
