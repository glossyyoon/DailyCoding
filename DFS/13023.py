import sys


N, M = map(int, sys.stdin.readline().split())
relation = [[] for _ in range(N)]
visited = [False] * N
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)


def dfs(start, number):
    if number == 4:
        print(1)
        sys.exit()
    for i in relation[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False


for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
print(0)
