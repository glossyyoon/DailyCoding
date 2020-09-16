import sys
num = int(sys.stdin.readline())
relation = []
count = 0

for _ in range(num):
    def dfs(start):
        check[start]=1
        for i in relation[start]:
            if check[start]==0:
                dfs(i)
    v, e = map(int, sys.stdin.readline().split(" "))
    check = [0 for _ in range(v+1)]
    for i in range(v+1):
        relation.append([])
    for i in range(e):
        a, b = map(int, sys.stdin.readline().split(" "))
        relation[a].append(b)
        relation[b].append(a)
    for j in range(1, v+1):
        if check[j]==0:
            dfs(j)
            count+=1
    if count ==1:
        print("YES")
    else:
        print("NO")



