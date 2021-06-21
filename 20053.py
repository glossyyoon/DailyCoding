def solve(num):
    minn, maxx = num[0], num[0]
    for i in range(len(num)):
        if num[i] < minn:
            minn = num[i]
        if num[i] > maxx:
            maxx = num[i]
    print(minn, maxx)


t = int(input())
for i in range(t):
    n = input()
    nums = list(map(int, input().split()))
    solve(nums)
