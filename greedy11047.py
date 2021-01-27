import sys
n, k = map(int, sys.stdin.readline().split(' '))
arr = []
maxnum = 0
coin = 0
for i in range(n):
    arr.append(int(sys.stdin.readline()))
for i in range(n-1, -1, -1):
    if arr[i]<k:
        maxnum = i
        break

for i in range(maxnum, -1, -1):
    if k%arr[i]==0:
        coin+=k//arr[i]
        print(coin)
        break
    temp = k//arr[i]
    coin += temp
    k -= temp*arr[i]
