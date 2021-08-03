import sys

N, M = map(int, sys.stdin.readline().split())
s = ""

strings = {sys.stdin.readline().rstrip() for _ in range(N)}

count = 0
for j in range(M):
    pattern = sys.stdin.readline().rstrip()
    if pattern in strings:
        print("Pattern:", pattern)
        count += 1
print(strings)
print(count)
