import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque()


def push_front(x):
    arr.appendleft(x)


def push_back(x):
    arr.append(x)


def pop_front():
    return arr.popleft() if arr else -1


def pop_back():
    return arr.pop() if arr else -1


def size():
    return len(arr)


def empty():
    return 0 if arr else 1


def front():
    return arr[0] if arr else -1


def back():
    return arr[-1] if arr else -1


for i in range(N):
    word = sys.stdin.readline().split()
    if word[0] == "push_back":
        push_back(int(word[1]))
    elif word[0] == "push_front":
        push_front(int(word[1]))
    elif word[0] == "pop_front":
        print(pop_front())
    elif word[0] == "pop_back":
        print(pop_back())
    elif word[0] == "size":
        print(size())
    elif word[0] == "empty":
        print(empty())
    elif word[0] == "front":
        print(front())
    elif word[0] == "back":
        print(back())