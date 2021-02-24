number = 7
c = [False]*8
a = [[]]*8
def dfs(start):
    c[start]=1
    a.append(start)
    for e in sorted(a[start]):
        if c[e]==0:
            dfs(e)
    
a[1].append(2)
a[2].append(1)
a[1].append(3)
a[3].append(1)
a[2].append(4)
a[4].append(2)
a[2].append(3)
a[3].append(2)
a[2].append(5)
a[5].append(2)
a[6].append(3)
a[3].append(6)
a[3].append(7)
a[7].append(3)
dfs(1)