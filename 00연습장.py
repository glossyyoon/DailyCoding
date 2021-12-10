from itertools import permutations


def solution(word):
    answer = []
    moeum = "AEIOU"
    for i in range(len(moeum)):
        w = list(permutations(list(moeum), i + 1))
        for j in w:
            answer.append("".join(j))
    answer.sort()
    return answer.index(word)


solution("AAAAE")
