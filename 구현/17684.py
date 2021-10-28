def solution(msg):
    answer = []
    dic = [
        "",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    # msg = list(msg)
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w : c + 1] not in dic:
            dic[msg[w : c + 1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer


print(solution("KAKAO"))
