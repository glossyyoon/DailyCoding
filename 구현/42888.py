def solution(record):
    answer = []
    inout = ["Enter", "Leave", "Change"]
    userDict = {}
    for i in record:
        messages = i.split()
        if not messages[1] in userDict.keys():
            userDict[messages[1]] = messages[2]
        if messages[0] == "Enter" and messages[1] in userDict.keys():
            userDict[messages[1]] = messages[2]
        elif messages[0] == "Change":
            print(userDict)
            userDict[messages[1]] = messages[2]
            print(userDict)
    for i in record:
        messages = i.split()
        if messages[0] == inout[0]:
            print(userDict[messages[1]] + "님이 들어왔습니다.")
        elif messages[0] == inout[1]:
            print(userDict[messages[1]] + "님이 나갔습니다.")
    return answer


print(
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
)
