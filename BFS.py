number = 7
c = [False]*8
a = [[]]*8
# start = 0
def bfs(start):
    queue = []
    queue.append(start)
    c[start] = True
    while(len(queue)!=0):
        x = queue.pop(0)
        print(x)
        for i in range(len(a[x])-1):
            y = a[x][i]
            if(c[y]!=True):
                queue.append(y)
                c[y] = True
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
bfs(1)
