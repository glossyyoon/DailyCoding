import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
sum = 0
minLength = sys.maxsize
left, right = 0, 0

while True:
    if sum >= S:
        minLength = min(minLength, right - left)
        print(left, right)
        sum = sum - nums[left]
        left += 1
    elif right == N:
        break
    else:
        sum = sum + nums[right]
        right += 1

if minLength == sys.maxsize:
    print(0)
else:
    print(minLength)
