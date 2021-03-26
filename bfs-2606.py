computer = int(input())
node = int(input())
graph = [[] for i in range(computer + 1)]
from collections import deque
for i in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(computer+1)
def bfs(graph, start, visit):
    count = 0
    queue = deque()
    queue.appendleft(start)
    visit[start] = True
    while queue:
        v = queue.pop()
        for i in graph[v]:
            if visit[i]==False:
                queue.appendleft(i)
                count += 1
                visit[i] = True
    return count
print(bfs(graph, 1, visited))