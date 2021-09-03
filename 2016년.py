def solution(a, b):
    day = [
        "THU",
        "FRI",
        "SAT",
        "SUN",
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
        "SAT",
        "SUN",
        "MON",
        "TUE",
        "WED",
    ]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start_day = 0
    for i in range(1, a):
        start_day += month[i - 1]
    start_day = day[start_day % 7 + 1]
    idx = day.index(start_day)
    new_day = day[idx:] + day[:idx]
    new_day.insert(0, day[idx - 1])
    answer = new_day[b % 7]
    return answer


print(solution(11, 11))
