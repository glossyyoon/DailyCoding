import re


def solution(dartResult):
    answer = 1
    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"": 1, "*": 2, "#": -1}

    dart = re.findall(r"(\d+)([S|D|T]+)([*|#]?)", dartResult)
    for i in range(len(dart)):
        if dart[i][2] == "*" and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    answer = sum(dart)
    return answer


print(solution("1D2S#10S"))
