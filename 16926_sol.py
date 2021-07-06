import sys

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(R):
    x, y = 0, 0
    n, m = N, M
    r = min(n, m) // 2
    while r:
        cache = arr[x][y]  #이 값 하나만 저장하고 나머지는 하나씩 다 당겨오면 된다^^ 대신 순서 중요
        for i in range(m - 1):
            arr[x][y + i] = arr[x][y + i + 1]
        for i in range(n - 1):
            arr[x + i][y + m - 1] = arr[x + i + 1][y + m - 1]
        for i in range(m - 1):
            arr[x + n - 1][y + m - i - 1] = arr[x + n - 1][y + m - i - 2]
        for i in range(n - 1):
            arr[x + n - 1 - i][y] = arr[x + n - i - 2][y]
        arr[x + 1][y] = cache
        n -= 2
        m -= 2
        x += 1
        y += 1
        r -= 1

for i in arr:
    for j in i:
        print(j, end=" ")
    print()
