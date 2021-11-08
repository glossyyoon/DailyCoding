def solution(m, musicinfos):
    start = 0
    end = 1
    name = 2
    code = 3

    for i in range(len(musicinfos)):
        newCode = ""
        newlist = musicinfos[i].split(",")
        newlist[start] = int(newlist[start].replace(":", ""))
        newlist[end] = int(newlist[end].replace(":", ""))
        while newlist[end] - newlist[start] >= len(newCode) + 1:
            newCode += newlist[code][: newlist[end] - newlist[start]]
            if m == newCode:
                return newlist[name]
            elif m in newCode and newCode[newCode.index(m) + len(m)] != "#":
                return newlist[name]
        newCode = ""
    return "(None)"


print(
    solution(
        "CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    )
)
