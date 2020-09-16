def solution(info, query):
    import sys
    sys.setrecursionlimit(10000)
    length = len(query)
    answer = [0 for _ in range(length)]
    count=0
    bonus = "-"
    for i in query:
        count+=1
        strings = i.replace("and ", "")
        lan, job, car, food, score = strings.split(" ")
        score = int(score)
        for j in info:
            
            lan1, job1, car1, food1, score1 = j.split(" ")
            score1 = int(score1)
            if score1<score:
                continue
            else:
                if (lan==lan1 or lan==bonus) and (job==job1 or job==bonus) and (car==car1 or car==bonus) and (food==food1 or food==bonus):
                    answer[count-1]+=1

    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))