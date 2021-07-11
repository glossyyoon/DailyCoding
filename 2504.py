import sys

func = list(sys.stdin.readline())
stack = []

for i in range(len(func)):
    if func[i] == ")":
        t = 0
        while stack:
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
                t += top
    elif func[i] == "]":
        t = 0
        while stack:
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
                t += top
    else:
        stack.append(func[i])
print(stack)