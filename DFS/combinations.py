n = 4
k = 2
result = []


def dfs(elements, start, k):
    # print(elements)
    if k == 0:
        result.append(elements[:])

    for i in range(start, n + 1):
        elements.append(i)
        dfs(elements, i + 1, k - 1)
        # [1, 2, 3, 4]에서 pop을 하는게 아니라 [1, 2, 3]에서 pop을 함
        elements.pop()


dfs([], 1, k)
print(result)
