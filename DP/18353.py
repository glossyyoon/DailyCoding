import sys

N = int(sys.stdin.readline().rstrip())
dp = [1] * N
soldiers = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))
