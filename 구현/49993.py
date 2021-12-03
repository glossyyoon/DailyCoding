def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skillList = list(skill)
        for s in skills:
            if s in skill:
                if s != skillList.pop(0):
                    break
        else:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
print(solution("CBD", ["AEF", "ZJW"]))
