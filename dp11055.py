import sys
num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split(' ')))
dp = [x for x in lst]
for i in range(num):
    for j in range(i):
        if lst[i]>lst[j]:
            dp[i] = max(dp[i], dp[j]+lst[i])
print(max(dp))