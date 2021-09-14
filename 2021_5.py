def dfs(graph, start, info, edges, answer, l, w):
    stack = []
    visit = [False] * len(graph)
    stack.append(start)
    l_list = []
    visit[start] = True
    while stack:
        node = stack.pop()
        # print(node, end=" ")
        if l <= w:
            break
        if info[node] == 0:
            l += 1
        else:
            w += 1
        print(l, w)
        for i in graph[node]:
            if not visit[i]:
                stack.append(i)
            visit[i] = True
        visit[start] = False
    return l - 1


def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(edges) + 1)]
    ans = []
    for i in edges:
        p, c = i[0], i[1]
        graph[p].append(c)
        graph[c].append(p)
    ans.append(dfs(graph, 0, info, edges, answer, 0, -1))
    print(ans)
    return max(ans)


print(
    solution(
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [
            [0, 1],
            [1, 2],
            [1, 4],
            [0, 8],
            [8, 7],
            [9, 10],
            [9, 11],
            [4, 3],
            [6, 5],
            [4, 6],
            [8, 9],
        ],
    )
)

# info 0- 양, 1 - 늑대
# edges 간선 정보
