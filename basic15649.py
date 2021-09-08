n, m = map(int, input().split())
a = [0 for _ in range(m + 1)]
c = [False for _ in range(n + 1)]


def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if c[i]:
                continue
            c[i] = True
            a[index] = i
            go(index + 1, n, m)
            c[i] = False


go(0, n, m)