a, b, c, d, e, f = map(int, input().split())
for i in range(-999, 999 + 1):
    for j in range(-999, 999 + 1):
        if a * i + b * j == c and d * i + e * j == f:
            print(i, j)
            break
