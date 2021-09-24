import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
result = []


def backtrack(start, comb):
    if len(comb) == m:
        result.append(comb.copy())
        return
    for i in range(start, n + 1):
        comb.append(i)
        backtrack(i + 1, comb)
        comb.pop()
    return result


backtrack(1, [])
for i in result:
    for j in i:
        print(j, end=" ")
    print()
