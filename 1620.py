import sys

N, M = map(int, sys.stdin.readline().split())
li = []
dic = {}
for i in range(1, N + 1):
    p = sys.stdin.readline().rstrip()
    li.append(p)
    dic[p] = i - 1
for i in range(M):
    s = sys.stdin.readline().rstrip()
    if s.isdigit():
        print(li[int(s) - 1])
    elif s.isalpha():
        print(dic[s] + 1)
