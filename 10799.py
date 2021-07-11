import sys

pipe = list(sys.stdin.readline())
stack = []
count = 0
for i in range(len(pipe)):
    if pipe[i] == "(":
        stack.append("(")
    elif pipe[i] == ")" and pipe[i - 1] == "(":
        stack.pop()
        count += len(stack)
    elif pipe[i] == ")" and pipe[i - 1] == ")":
        stack.pop()
        count += 1
print(count)