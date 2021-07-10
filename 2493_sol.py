import sys

N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []
for i in range(N):
    while stack:
        if stack[-1][1] > top[i]:  #무조건 마지막이랑 비교해서 top이 더 작으면 pop. 더 크면 append
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, top[i]])
for i in answer:
    print(i, end=" ")
