import sys

arr = list(sys.stdin.readline())
stack = []
result = 0
for i in range(len(arr)):
    if arr[i] == ")":
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == "(":
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(t * 2)
                break
            elif top == "[":
                print(0)
                exit(0)
            else:
                t += int(top)
    elif arr[i] == "]":
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == "[":
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(t * 3)
                break
            elif top == "(":
                print(0)
                exit(0)
            else:
                t += int(top)
    else:
        stack.append(arr[i])

for i in stack:
    if i == '[' or i == '(':
        print(0)
        exit(0)
    elif str(i).isdigit():
        result += int(i)
print(result)
