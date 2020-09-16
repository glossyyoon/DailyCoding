import sys
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split(' '))
relation = []
check = [0 for _ in range(n+1)]
result = []
starts = []
count = 0
for _ in range(n+1):
    relation.append([])
for i in range(n):
    result.append([])
for i in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    relation[a].append(b)
    relation[b].append(a)
def dfs(start):
    check[start] = 1
    for e in relation[start]:
        if check[e] == 0:
            dfs(e)

for j in range(1, n+1):
    if check[j]==0:
        dfs(j)
        count+=1
print(count)

