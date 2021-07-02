import sys

N = int(sys.stdin.readline())
switch = [0] + list(map(int, sys.stdin.readline().split()))
student = int(sys.stdin.readline())


def findSwitch(s, n):
    if s == 1:
        switch[n] = int(not switch[n])
        for i in range(2 * n, N + 1, n):
            switch[i] = int(not switch[i])
    elif s == 2:
        switch[n] = int(not switch[n])
        for j in range(N // 2):
            if n + j > N or n - j < 1: break
            if switch[n - j] == switch[n + j]:
                switch[n - j] = int(not switch[n - j])
                switch[n + j] = int(not switch[n + j])
            else:
                break


for i in range(student):
    gender, num = map(int, sys.stdin.readline().split())
    findSwitch(gender, num)
for k in range(1, N + 1):
    print(switch[k], end=" ")
    if k % 20 == 0:
        print()
