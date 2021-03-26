graphs = [[1, 3], [0, 2], [1], [0, 4, 6], [3, 5], [4], [3]]
visited = [False] * 7


def dfs(graph, start, visit):
    visit[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if visit[i] == False:
            dfs(graphs, i, visit)


dfs(graphs, 0, visited)