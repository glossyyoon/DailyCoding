from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    result = []
    report = list(set(report))
    user = defaultdict(list)  # 사용자가 신고한 유저
    warn = defaultdict(int)  # 신고당한 유저
    for i in id_list:
        user[i] += []
    for s in report:
        a, b = s.split()
        if a in user:
            user[a].append(b)
        if b in warn:
            warn[b] += 1
        else:
            warn[b] = 0
    for i in list(warn.keys()):
        if warn[i] >= k - 1:
            answer.append(i)
    for j in id_list:  # muzi, frodo, apeach, neo
        count = 0
        for i in answer:  # frodo, neo
            if i in user[j]:
                count += 1
        result.append(count)
    return result


print(
    solution(
        ["con", "ryan"],
        ["ryan con", "ryan con", "ryan con", "ryan con"],
        3,
    )
)
