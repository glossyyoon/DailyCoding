def solution(table, languages, preference):
    answer = ""
    score = []
    name = []
    for i in range(len(table)):
        cont = list(table[i].split())
        cont_score = 0
        for j in range(len(cont)):
            if j == 0:
                name.append(cont[j])
                a = 1
            else:
                for k in range(len(languages)):
                    if cont[j] == languages[k]:
                        cont_score += (6 - j) * preference[k]
        score.append(cont_score)
    count = 0
    max_list = []
    maximum = max(score)
    for i in range(len(score)):
        if score[i] == maximum:
            max_list.append(i)
    result = []
    for i in max_list:
        result.append(name[i])
    result = sorted(result)
    answer = result[0]

    return answer
