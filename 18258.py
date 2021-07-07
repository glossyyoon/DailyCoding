import sys
from collections import deque

N = int(sys.stdin.readline())
order = deque([])


def push(x):
    order.append(x)


def pop():
    if len(order) == 0:
        return -1
    return order.popleft()


def size():
    return len(order)


def empty():
    return 0 if order else 1


def front():
    return order[0] if order else -1


def back():
    return order[-1] if order else -1


for i in range(N):
    word = sys.stdin.readline().split()
    s = word[0]
    if s == "push":
        n = word[1]
        push(int(n))
    elif s == "front":
        print(front())
    elif s == "back":
        print(back())
    elif s == "size":
        print(size())
    elif s == "empty":
        print(empty())
    elif s == "pop":
        print(pop())