import re


def headNumber(f):
    for i in range(len(f)):
        if f[i].isdigit():
            return i


def numberTail(f):
    for i in range(len(f)):
        if not f[i].isdigit():
            return i


def solution(files):
    answer = []
    for idx in range(len(files)):
        head, rest = (
            files[idx][: headNumber(files[idx])],
            files[idx][headNumber(files[idx]) :],
        )
        head = head.lower()
        number, tail = rest[: numberTail(rest)], rest[numberTail(rest) :]
        number = int(number)
        files[idx] = (files[idx], head, number)
    files.sort(key=lambda file: (file[1], file[2]))
    return [file[0] for file in files]


print(
    solution(
        [
            "F-5 Freedom Fighter",
            "B-50 Superfortress",
            "A-10 Thunderbolt II",
            "F-14 Tomcat",
        ]
    )
)
