def solution(s):
    answer = ""
    eng = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    num = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]
    for idx, v in enumerate(s):
        if v in eng:
            s = s.replace(v, num[idx])
            answer = s
        else:
            answer += v
    return int(answer)


print(solution("2three45sixseven"))
