t = int(input())
a = []
for i in range(t):
    a.append(int(input()))


def go(count, s, n):
    if s > n:
        return 0
    if s == n:
        return 1
    result = 0
    for i in range(1, 4):
        result += go(count + 1, s + i, n)
    return result


for j in a:
    print(go(0, 0, j))