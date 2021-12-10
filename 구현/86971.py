from collections import deque


def bfs(start, visited, graph):
    queue = deque([start])
    result = 1
    visited[start] = True
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if not visited[i]:
                result += 1
                queue.append(i)
                visited[i] = True
    return result


def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n + 1)]

    for wire in wires:
        a, b = wire[0], wire[1]
        tree[a].append(b)
        tree[b].append(a)

    for start, notVisit in wires:
        visited = [False] * (n + 1)
        visited[notVisit] = True
        result = bfs(start, visited, tree)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
