graph = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}


def graph_recursive(v, visited):
    print(v, end=" ")
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            graph_recursive(w, visited)


def graph_stack(v):
    stack = [v]
    visited = []
    while stack:
        w = stack.pop()
        if w not in visited:
            visited.append(w)
            for i in graph[w]:
                stack.append(i)
    return visited


graph_recursive(1, [])
print(graph_stack(1))
