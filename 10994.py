num = int(input())
count = 4 * (num - 1) + 1
starMap = [[' '] * count for _ in range(count)]


def draw(n, idx):
    if n == 1:
        starMap[idx][idx] = "*"
        return
    l = 4 * n - 3
    for i in range(idx, idx + l):
        starMap[idx][i] = "*"
        starMap[idx + l - 1][i] = "*"
    for j in range(idx, idx + l):
        starMap[j][idx] = "*"
        starMap[j][idx + l - 1] = "*"
    return draw(n - 1, idx + 2)


draw(num, 0)
for i in starMap:
    for j in i:
        print(j, end="")
    print()