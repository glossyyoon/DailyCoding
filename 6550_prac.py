import sys


def solution(s, t, start):
    s = list(s)
    if not s:
        return True
    while s:
        word = s.pop(0)
        if word in t[start:]:
            return solution(s, t, t.index(word))
        else:
            return False


while True:
    try:
        s, t = sys.stdin.readline().rstrip().split()
        if solution(s, t, 0):
            print("Yes")
        else:
            print("No")
    except:
        break
