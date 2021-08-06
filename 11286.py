import heapq, sys

N = int(sys.stdin.readline().rstrip())

heap = []
for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
