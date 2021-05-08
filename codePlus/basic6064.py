t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    k = x
    while k < n * m:
        if k % n == y:
            print(k)
            break
        k = k + m
    else:
        print(-1)