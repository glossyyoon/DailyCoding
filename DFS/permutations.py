a = list(map(int, input().split()))  # [1, 2, 3] -> 조합 구하기
visited = [False] * len(a)
results = []
prev_elements = []


def dfs(elements):
    if len(elements) == 0:
        results.append(prev_elements[:])

    for e in elements:
        next_elements = elements[:]  # 전체를 일단 저장
        next_elements.remove(e)  # 앞에서 부터 하나씩 pop

        prev_elements.append(e)
        dfs(next_elements)
        prev_elements.pop()
    return results


print(dfs(a))
