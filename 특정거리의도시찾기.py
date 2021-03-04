from collections import deque
n, m, k, x = map(int, input().split())
city = []
for i in range(n):
    city.append([])
for i in range(m):
    a, b = map(int, input().split())
    city[a].append(b)
visit = [False] * (n + 1)
result = []


def bfs(city, length, start):
    queue = deque([start])
    visit[start] = True
    count = 1
    while queue:
        for _ in range(len(queue)):  #왜함????
        v = queue.popleft()
        for i in city[v]:
            if not visit[i] and count == length:
                result.append(i)
            if not visit[i]:
                visit[i] = True
                queue.append(i)
        count += 1


bfs(city, k, x)
for node in result:
    print(node)