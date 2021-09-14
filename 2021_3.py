from collections import defaultdict
import math


def addTime(time, s, typ):
    hh, mm = s.split(":")
    if typ == "IN":
        time += int(hh) * 60 + int(mm)
    if typ == "OUT":
        time = abs(time - (int(hh) * 60 + int(mm)))
    return time


def solution(fees, records):
    answer = []
    # 등록
    regist = defaultdict(list)
    for record in records:
        time, num, typ = record.split()
        if num in regist:
            regist[num].append([time, typ])
        else:
            regist[num] = [[time, typ]]
    regist = dict(sorted(regist.items()))
    # 계산
    for i in regist:
        time = 0
        times = []
        for record in regist[i]:
            if record[1] == "IN":
                time += addTime(time, record[0], record[1])
            elif record[1] == "OUT":
                times.append(addTime(time, record[0], record[1]))
                time = 0
        if regist[i][-1][1] == "IN":
            times.append(addTime(time, "23:59", "OUT"))
        time = 0

        for t in times:
            time += t
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
            answer.append(fee)
    return answer


print(
    solution(
        [180, 5000, 10, 600],
        [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ],
    )
)
