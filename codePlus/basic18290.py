n, m, k = map(int, input().split())  #n과m 과 같은 알고리즘으로 풀기 위해서 2차원을 1차원 배열로 변경
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]
ans = -2147483647
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def go(prev, cnt, s):
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return
    for j in range(prev + 1, n * m):  #선택된 좌표를 오름차순으로 배열
        x = j // m  #x의 좌표
        y = j % m
        if c[x][y]:
            continue
        ok = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if c[nx][ny]:
                    ok = False

        if ok:
            c[x][y] = True  #방문표시
            go(x * n + y, cnt + 1, s + a[x][y])  #재귀
            c[x][y] = False  #다시 False로 해줘야 다음 j에서 또 비교


go(-1, 0, 0)
print(ans)