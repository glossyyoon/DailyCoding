import sys
import heapq

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    t = int(sys.stdin.readline().rstrip())
    minheap, maxheap = [], []
    visit = [False] * 1000000
    for key in range(t):
        f, b = sys.stdin.readline().rstrip().split()
        b = int(b)
        if f == "I":
            heapq.heappush(minheap, (b, key))
            heapq.heappush(maxheap, (-b, key))
            visit[key] = True
        elif f == "D":
            if b == 1:
                while maxheap and not visit[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    visit[maxheap[0][1]] = False
                    heapq.heappop(maxheap)

            elif b == -1:
                while minheap and not visit[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    visit[minheap[0][1]] = False
                    heapq.heappop(minheap)

    while minheap and not visit[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visit[maxheap[0][1]]:
        heapq.heappop(maxheap)
    if minheap and maxheap:
        print(-maxheap[0][0], minheap[0][0])
    else:
        print("EMPTY")
