import re


def solution(files):
    answer = []
    for file in files:
        foundFile = re.findall(r"([^\d]+)([\d]{1,5})(.+)?", file, flags=re.I)[0]
        answer.append(foundFile)
    answer = sorted(answer, key=lambda x: (x[0], int(x[1])))
    return list(map(lambda x: "".join(x), answer))


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
