def removeDuplicateLetters(s):
    sortedStr = ""
    answer = ""
    temp = sorted(s)
    for i in range(len(temp)):
        if temp[i] != temp[i - 1]:
            sortedStr += temp[i]
    for i in range(len(sortedStr)):
        answer += s[s.index(sortedStr[i])]
    return answer


print(removeDuplicateLetters("cbacdcbc"))
