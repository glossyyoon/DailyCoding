import sys

N = int(sys.stdin.readline())
for i in range(N):
    s = sys.stdin.readline().rstrip()
    for j in s:
        if j.isalnum():
            print("true")
        else:
            print(False)
