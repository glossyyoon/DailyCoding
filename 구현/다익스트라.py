from collections import defaultdict
import heapq
import collections


def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
    graph = collections.defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))
    Q = [(0, K)]
    dist = collections.defatuldict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    if len(dist) == N:
        return max(dist.values())
    return -1
