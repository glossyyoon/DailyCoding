from collections import deque

graph = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}


def BFS(start):
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited


print(BFS(1))
