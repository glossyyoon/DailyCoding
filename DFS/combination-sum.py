candidates = list(map(int, input().split()))
target = int(input())
result = []


def dfs(csum, index, path):
    if csum == 0:
        result.append(path)
        return
    if csum < 0:
        return
    for i in range(index, len(candidates)):
        dfs(csum - candidates[i], i, path + [candidates[i]])


print(dfs(target, 0, []))
print(result)
