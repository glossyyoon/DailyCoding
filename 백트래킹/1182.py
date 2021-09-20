import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
result = []


def dfs(element, start, S):
    global count
    if start >= N:
        return
    element += numbers[start]
    if element == S:
        count += 1
    dfs(element - numbers[start], start + 1, S)
    dfs(element, start + 1, S)


dfs(0, 0, S)
print(count)
