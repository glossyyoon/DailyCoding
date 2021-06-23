def isGroupWord(w):
    setW = []
    setW.append(w[0])
    result = True
    for i in range(1, len(w)):
        if w[i] == w[i - 1]:
            continue
        if w[i] != w[i - 1] and w[i] in setW:
            result = False
        if w[i] != w[i - 1]:
            setW.append(w[i])
    return result


n = int(input())
count = 0
for i in range(n):
    word = input()
    if isGroupWord(word):
        count += 1
print(count)