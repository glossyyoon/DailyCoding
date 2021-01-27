num = int(input())
dp = [0]*10001
grape = [0]
for i in range(num):
    grape.append(int(input()))
if num == 1:
    print(grape[1])
elif num == 2:
    print(grape[1]+grape[2])
else:
    dp[1] = grape[1]
    dp[2] = grape[1]+grape[2]
    dp[3] = max(dp[1]+grape[3], dp[2], grape[2]+grape[3])
    for j in range(4, num+1):
        dp[j] = max(dp[j-3]+grape[j-1]+grape[j], dp[j-1], dp[j-2]+grape[j])
    print(dp[num])