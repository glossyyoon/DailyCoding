def solution(begin, target, words):
    answer = 0
    stack = [begin]
    
    if target not in words:
        return 0
    
    while len(words) != 0:
        sub = []
        for data in stack:
            for word in words:
                count = 0
                for i in range(len(data)):
                    if word[i] != data[i]:
                        count += 1
                    if count == 2:
                        break
                if count == 1:
                    sub.append(word)
                    words.remove(word)
        answer += 1
        if target in sub:
            return answer
        else:
            stack = sub
    
    return answer