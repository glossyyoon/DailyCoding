from collections import deque
graphs = [[1, 3], [0, 2], [1], [0, 4, 6], [3, 5], [4], [3]]
visited = [False] * 7
queue = deque()


def bfs(graph, start, visit):
    queue.appendleft(start)
    visit[start] = True
    while queue:
        v = queue.pop()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.appendleft(i)
                visited[i] = True


bfs(graphs, 0, visited)