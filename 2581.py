M = int(input())
N = int(input())
stack = []
for i in range(M, N + 1):
    if i == 2:
        stack.append(i)
    elif i == 0 or i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
        elif j == i - 1 and i % j != 0:
            stack.append(i)
result = 0
if stack:
    for i in stack:
        result += i
    print(result)
    print(stack[0])
else:
    print(-1)
