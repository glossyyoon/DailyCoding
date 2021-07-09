import sys

pipe = list(sys.stdin.readline())
result = []
count = 0
for i in range(len(pipe)):
    if pipe[i] == "(":
        result.append("(")
    else:
        if pipe[i] == ")" and pipe[i - 1] == "(":
            result.pop()
            count += len(result)
        elif pipe[i] == ")" and pipe[i - 1] == ")":
            result.pop()
            count += 1

print(count)