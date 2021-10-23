def solution(s):
    answer = True
    brackets = list(s)
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True
```