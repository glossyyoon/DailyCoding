n, m = map(int, input().split())
a = [0 for _ in range(m)]
check = [False for _ in range(n + 1)]


def go(index, start, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
    else:
        for i in range(start, n + 1):
            if check[i]:
                continue
            check[i] = True
            a[index] = i
            go(index + 1, i + 1, n, m)
            check[i] = False


go(0, 1, n, m)