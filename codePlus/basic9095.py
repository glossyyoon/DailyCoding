t = int(input())
num = []
for i in range(t):
    num.append(int(input()))


def go(count, s, n):
    if s > n:
        return 0
    if count == n:
        return 1
    now = 0
    for i in range(3):
        now += go(count + 1, s + i, n)
    return now


for j in num:
    print(go(0, 0, j))