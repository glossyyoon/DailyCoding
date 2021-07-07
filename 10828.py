import sys

N = int(sys.stdin.readline())
order = []


def push(x):
    order.append(x)


def pop():
    if len(order) == 0:
        return -1
    return order.pop()


def size():
    return len(order)


def empty():
    return 0 if order else 1


def top():
    if len(order) == 0:
        return -1
    return order[-1]


for i in range(N):
    word = sys.stdin.readline().split()
    s = word[0]
    if s == "push":
        n = word[1]
        push(int(n))
    elif s == "top":
        print(top())
    elif s == "size":
        print(size())
    elif s == "empty":
        print(empty())
    elif s == "pop":
        print(pop())