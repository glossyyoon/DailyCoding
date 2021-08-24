from collections import deque

x = int(input())
queue = deque()

dist = [[-1] * (x + 1) for i in range(x + 1)]
queue.append((1, 0))

dist[1][0] = 0

while queue:
    s, c = queue.popleft()
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        queue.append((s, s))
    if s + c <= x and dist[s + c][c] == -1:
        dist[s + c][c] = dist[s][c] + 1
        queue.append((s + c, c))
    if s - 1 >= 0 and dist[s - 1][c] == -1:
        dist[s - 1][c] = dist[s][c] + 1
        queue.append((s - 1, c))

r = 100
for i in range(1, x + 1):
    if dist[x][i] != -1:
        r = min(r, dist[x][i])
print(r)
