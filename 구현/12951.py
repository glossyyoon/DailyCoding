def solution(s):
    answer = []
    words = list(s.split(" "))
    for word in words:
        newWord = ""
        for i in range(len(word)):
            if not word[i].isalnum():
                continue
            if i == 0:
                newWord += word[i].upper()
            else:
                newWord += word[i].lower()
        answer.append(newWord)
    return " ".join(answer)


print(solution("3people"))
