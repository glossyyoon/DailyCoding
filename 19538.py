import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = [[]]  # 그래프 관계
dist = [-1] * (n + 1)  # 믿는 데 걸린 시간
believe = [0] * (n + 1)  # 믿고 있는지

for i in range(n):
    s = list(map(int, sys.stdin.readline().rstrip().split()))
    r = s[:-1]
    g = []
    for k in r:
        g.append(k)
    graph.append(g)


m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))


def bfs(v):
    global believe, dist, graph
    que = deque()
    visited = [v]
    time = 1
    que.append((v, time))
    believe[v] = 1  # 유포자는 루머를 믿음
    dist[v] = 0  # 유포자는 0초 걸림
    state = [0] * n
    while que:
        curr, time = que.popleft()  # 1, 0
        for i in graph[curr]:  # 2,3
            for check_num in graph[curr]:
                state[check_num] += 1
                if believe[check_num] == -1:
                    if state[check_num] * 2 >= len(graph[check_num]):
                        visited.append(check_num)
                        believe[check_num] = believe[curr] + 1
            # time += 1
            # if i not in visited:
            #     count = 0
            #     for s in graph[i]:
            #         if believe[s] == 1:
            #             count += 1
            #     half = len(graph[i]) * 0.5
            #     if half <= count:
            #         dist[i] = time
            #         believe[i] = 1
            #         visited.append(i)
            #         que.append((i, time + 1))

    return state


for i in range(m):  # 루머를 퍼트린 사람의 수 만큼
    e = bfs(m_list[i])
print(e[1:])
