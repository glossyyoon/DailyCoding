s = list(input())
i = 0
while i < len(s):
    if s[i] == "<":
        i += 1
        while s[i] != ">":
            i += 1
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        temp = s[start:i]
        temp = reversed(temp)
        s[start:i] = temp
    else:
        i += 1
for i in s:
    print("".join(i), end="")
