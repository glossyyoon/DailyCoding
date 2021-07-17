import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
control = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
train = [[0] * 20 for _ in range(N)]

for order in control:
    case = order[0]
    i = order[1] - 1
    if case == 1:
        x = order[2] - 1
        train[i][x] = 1
    elif case == 2:
        x = order[2] - 1
        train[i][x] = 0
    elif case == 3:
        queue = deque(train[i])
        queue.pop()
        queue.appendleft(0)
        train[i] = list(queue)
    elif case == 4:
        queue = deque(train[i])
        queue.popleft()
        queue.append(0)
        train[i] = list(queue)

count = 1
pass_train = []
pass_train.append(train[0])
for i in range(1, N):
    if train[i] in pass_train:
        continue
    else:
        pass_train.append(train[i])
        count += 1
print(count)
