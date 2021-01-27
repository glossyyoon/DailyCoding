import sys
n, m, k = map(int, sys.stdin.readline().split(' '))
team = 0
while n>=0 and m>=0 and m+n>=k:
    n-=2
    m-=1
    team+=1
print(team-1)