import sys

words = list(sys.stdin.readline())
i = 0
while i < len(words):
    if words[i] == "<":
        i += 1
        while words[i] != ">":
            i += 1
        i += 1
    elif words[i].isalnum():
        start = i
        while i < len(words) and words[i].isalnum():
            i += 1
        tmp = words[start:i]
        tmp = reversed(tmp)
        words[start:i] = tmp
    else:
        i += 1
print("".join(words))