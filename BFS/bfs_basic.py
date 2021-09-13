from collections import deque

graph = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}


def bfs(v):
    visited = [v]
    queue = deque()
    queue.append(v)
    while queue:
        w = queue.popleft()
        for i in graph[w]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited


print(bfs(1))
