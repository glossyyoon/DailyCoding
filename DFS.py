graph = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}


def recursive_dfs(v, discovered):  # 사전식으로 방문
    print(v, end=" ")
    discovered.append(v)
    for i in graph[v]:
        if i not in discovered:
            recursive_dfs(i, discovered)


def stack_dfs(v):  # 역순으로 방문
    discorverd = []
    stack = [v]
    while stack:
        v = stack.pop()
        if v not in discorverd:
            discorverd.append(v)
            for i in graph[v]:
                stack.append(i)
    return discorverd


recursive_dfs(1, [])
print(stack_dfs(1))
