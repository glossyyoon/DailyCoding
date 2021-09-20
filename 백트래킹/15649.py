import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
result = []
arr = [i for i in range(1, N + 1)]
prev_elements = []


def dfs(elements):
    if len(prev_elements) == M:
        result.append(prev_elements[:])

    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)

        prev_elements.append(e)
        dfs(next_elements)
        prev_elements.pop()
    return result


dfs(arr)
for i in result:
    for j in i:
        print(j, end=" ")
    print()
