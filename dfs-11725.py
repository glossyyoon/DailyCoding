# node = int(input())
# tree = [[] for i in range(node+1)]
# for i in range(node-1):
#     a, b = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)
# visit = [False]*(node+1)
# stack = []
# def dfs(graph, v, visited):
#     visited[v] = True
#     stack.append(v)
#     for i in tree[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
# dfs(tree, 1, visit)
# print(stack)
import sys
sys.setrecursionlimit(10 ** 9)

node = int(sys.stdin.readline())
tree = [[] for i in range(node+1)]
parents = [0 for _ in range(node+1)]
parents[1] = 1

for i in range(node-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(graph, start, parent):
    for n in graph[start]:
        if parents[n]==0:
            parents[n] = start
            dfs(tree, n, parent)
dfs(tree, 1, parents)
for i in range(2, node+1):
    print(parents[i])