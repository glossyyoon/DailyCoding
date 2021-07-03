import sys

N = int(sys.stdin.readline())
count = 2

while N != 1:
    if N % count == 0:
        N = N / count
        print(count)
    else:
        count += 1