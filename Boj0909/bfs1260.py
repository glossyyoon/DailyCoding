import sys
n, m, v = map(int, sys.stdin.readline().split(" "))
check_dfs = [0 for _ in range(n+1)]
check_bfs = [0 for _ in range(n+1)]
relation = []
queue = []
result_dfs = []
result_bfs = []

for _ in range(n+1):
    relation.append([])
for i in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    relation[a].append(b)
    relation[b].append(a)
    
def dfs(start):
    check_dfs[start]=1
    result_dfs.append(start)
    for e in sorted(relation[start]):
        if check_dfs[e]==0:
            dfs(e)

        
def bfs(start):
    check_bfs[start]=1
    queue.append(start)
    while(len(queue)!=0):
        temp = queue.pop(0)
        result_bfs.append(temp)
        for i in sorted(relation[temp]):
            if check_bfs[i]==0:
                check_bfs[i] = 1
                queue.append(i)
    

dfs(v)
bfs(v)
for i in result_dfs:
    print(i, end = ' ')
print()
for i in result_bfs:
    print(i, end = ' ')
