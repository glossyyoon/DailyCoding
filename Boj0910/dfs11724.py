import sys
n, m = sys.stdin.readline().split('')
relation = []
check = [0 for _ in range(n)]
result = []
for i in range(n):
    result.append([])
for i in range(m):
    a, b = map(int, sys.stdin.readline().split(''))
    relation[a].append(b)
    relation[b].append(a)
def dfs(start):
    if check[start]==0:
        
