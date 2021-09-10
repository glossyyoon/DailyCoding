def solution(info, query):
    answer = []
    for q in query:
        count = 0
        cond = q.split()
        for i in info:
            people = i.split()
            if cond[0] != '-' and cond[0] != people[0]:
                continue
            if cond[2] != '-' and cond[2] != people[1]:
                continue
            if cond[4] != '-' and cond[4] != people[2]:
                continue
            if cond[6] != '-' and cond[6] != people[3]:
                continue
            if int(cond[7]) <= int(people[4]):
                count += 1
        answer.append(count)
    return answer


print(
    solution([
        "java backend junior pizza 150", "python frontend senior chicken 210",
        "python frontend senior chicken 150", "cpp backend senior pizza 260",
        "java backend junior chicken 80", "python backend senior chicken 50"
    ], [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150", "- and - and - and chicken 100",
        "- and - and - and - 150"
    ]))
