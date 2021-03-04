from collections import deque
num = int(input())
land = list(map(int, input().split()))
half = len(land) // 2
queue = deque()
queue = land
result = 0
for i in range(len(land) // 2):
    if land.index(max(land)) < half:
        result += max(land)
        half += half // 2
        for j in range(half - 1):
            queue.popleft()
        print(queue)
print(result)