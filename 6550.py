import sys


def solution(s, t):
    if len(s) > len(t):
        print("No")
        return
    right = 0
    i = 0
    for c in range(len(s)):

        while i < len(t):
            if s[c] == t[i]:
                i += 1
                break
            elif i == len(t) - 1:
                print("No")
                return
            i += 1
    print("Yes")


while True:
    try:
        s, t = sys.stdin.readline().rstrip().split()
        solution(s, t)
    except:
        break
