import sys

N = int(sys.stdin.readline())
land = list(sys.stdin.readline() for _ in range(N))
user = list(sys.stdin.readline() for _ in range(N))
answer = [['.'] * N for _ in range(N)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]  #왼쪽 위부터 차례로 시계방향
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def findBoom():
    for i in range(N):
        for j in range(N):
            if land[i][j] == '.' and user[i][j] == 'x':
                boom = 0

                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if land[nx][ny] == '*':
                        boom += 1
                answer[i][j] = boom
            if land[i][j] == '*' and user[i][j] == 'x':
                for a in range(N):
                    for b in range(N):
                        if land[a][b] == "*":
                            answer[a][b] = "*"


findBoom()
for i in answer:
    for j in i:
        print(j, end="")
    print()
