import sys
from collections import defaultdict


def dfs(start, visited):
    visited.add(start)
    check[start] = 1
    for v in g[start]:
        if not v in visited:
            dfs(v, visited.copy())
        else:
            result.extend(list(visited))
            return


n = int(sys.stdin.readline().rstrip())
g = defaultdict(list)
for i in range(1, n + 1):
    v = int(sys.stdin.readline().strip())
    g[v].append(i)
check = [0 for _ in range(n + 1)]
result = []
for i in range(n + 1):
    if not check[i]:
        dfs(i, set([]))
result.sort()

print(len(result))
for i in result:
    print(i)