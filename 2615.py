import sys

omok = list(sys.stdin.readline().split() for _ in range(19))
dx = [1, 0, 1, 1]  # 우하, 가로, 세로, 우하
dy = [1, 1, 0, -1]


def o():
    for i in range(19):
        for j in range(19):
            if omok[i][j]:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    count = 1
                    while 0 <= nx < 19 and 0 <= ny < 19 and omok[i][j] == omok[nx][ny]:
                        count += 1
                    if count == 5:
                        if (
                            0 <= nx + dx[k] < 19
                            and 0 <= ny + dy[k]
                            and omok[nx][ny] == omok[nx + dx[k]][ny + dy[k]]
                        ):
                            break
                        if (
                            0 <= nx + dx[k] < 19
                            and 0 <= ny + dy[k]
                            and omok[nx][ny] == omok[nx + dx[k]][ny + dy[k]]
                        ):
                            break
                        return omok[i][j], i + 1, j + 1
                    nx = i + dx[k]
                    ny = j + dy[k]


color, x, y = o()
if not color:
    print(color)
    print(x, y)
else:
    print(0)
    print(x, y)
