import sys

num = int(sys.stdin.readline())

for i in range(num):
    a1 = []
    b1 = []
    a, b = map(int, sys.stdin.readline().split())
    for i in range(1, b + 1):
        a1.append(i * a)
    for i in range(1, a + 1):
        b1.append(i * b)
    for k in a1:
        if k in b1:
            print(k)
            break
