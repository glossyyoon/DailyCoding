from collections import deque

s, n = map(int, input().split())
visit = [False] * 200000
dist = [-1] * 200000
queue = deque()
queue.append(s)
dist[s] = 0
visit[s] = True

queue_next = deque()
while queue:
    now = queue.popleft()
    visit[now] = True
    if now * 2 < 200000 and not visit[now * 2]:
        queue.appendleft(now * 2)
        visit[now * 2] = True
        dist[now * 2] = dist[now]
    if now - 1 >= 0 and not visit[now - 1]:
        queue.append(now - 1)
        visit[now - 1] = True
        dist[now - 1] = dist[now] + 1
    if now + 1 < 200000 and not visit[now + 1]:
        queue.append(now + 1)
        visit[now + 1] = True
        dist[now + 1] = dist[now] + 1
print(dist[n])
