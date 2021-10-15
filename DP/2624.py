T = int(input())
k = int(input())
L = []
L.append([0, 0])
for i in range(k):
    L.append(list(map(int, input().split())))
L.sort()
dp = [[0 for j in range(T + 1)] for i in range(k + 1)]
for i in range(k + 1):
    dp[i][0] = 1

for i in range(1, k + 1):
    for num in range(L[i][1] + 1):
        for j in range(T + 1):
            temp = j + num * L[i][0]
            if temp == 0:
                continue
            if temp < T + 1:
                dp[i][temp] += dp[i - 1][j]
            else:
                break

print(dp[k][T])
