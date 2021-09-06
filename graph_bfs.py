from collections import deque

graph = [
    [],
    [5, 6],  # 1에는 5와 6이 연결되어 있다.
    [3, 4, 6],  # 2에는 3과 4와 6이 연결되어 있다.
    [2, 4, 5],  # 3에는 2와 4와 5가 연결되어 있다.
    [2, 3],  # 4에는 2와 3이 연결되어 있다.
    [1, 3, 6],  # 5에는 1과 3과 6이 연결되어 있다.
    [1, 2, 5],  # 6에는 1과 2와 5가 연결되어 있다.
]


def bfs(v):
    que = deque()
    visited = [v]
    que.append(v)
    while que:
        v = que.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                que.append(i)
    return visited  # [1, 2, 3, 4, 5, 6, 7]


print(bfs(1))
