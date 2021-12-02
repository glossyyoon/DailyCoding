def solution(s):
    zeroCount = 0
    count = 0
    while s != "1":
        count += 1
        sLen = len(s.replace("0", ""))
        zeroCount += len(s) - sLen
        s = bin(sLen)[2:]
        print(s)
    return [count, zeroCount]


print(solution("110010101001"))
