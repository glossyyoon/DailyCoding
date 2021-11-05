import sys
from collections import deque

queue = []
N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
for i in range(N - 1, 0, -1):
    t = top[i]
    for j in range(i - 1, -1, -1):
        if top[j] >= t:
            queue.append(j + 1)
            break
        elif j == 0:
            queue.append(0)
queue.append(0)
for i in range(len(queue) - 1, -1, -1):
    print(queue[i], end=" ")
