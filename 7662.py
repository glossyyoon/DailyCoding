import sys, heapq

t = int(sys.stdin.readline().rstrip())
for q in range(t):
    minheap, maxheap = [], []
    visit = [False] * 1000000
    k = int(sys.stdin.readline().rstrip())
    for key in range(k):
        s, n = sys.stdin.readline().rstrip().split()
        n = int(n)
        if s == "I":
            heapq.heappush(minheap, (n))
            heapq.heappush(maxheap, (-n))
            visit[key] = True
            print(minheap, maxheap)
        elif s == "D":
            if n == 1:
                while maxheap and not visit[key]:
                    heapq.heappop(maxheap)
                if maxheap:
                    num = heapq.heappop(maxheap)
                    visit[key] = False
            if n == -1:
                while minheap and not visit[key]:
                    heapq.heappop(minheap)
                if minheap:
                    num = heapq.heappop(minheap)
                    visit[key] = False
            print(minheap, maxheap)

    print(minheap, maxheap)
    while minheap and not visit[key]:
        heapq.heappop(minheap)
    while maxheap and not visit[key]:
        heapq.heappop(maxheap)
    if minheap and maxheap:
        print(-maxheap[0][0], minheap[0][1])
    else:
        print("EMPTY")
