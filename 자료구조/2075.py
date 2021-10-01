import sys, heapq

n = int(sys.stdin.readline().rstrip())
nums = []
arr = []
for i in range(n):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    for num in nums:
        if len(arr) < n:
            heapq.heappush(arr, (num))
        else:
            element = heapq.heappop(arr)
            if num > element:
                heapq.heappush(arr, (num))
            else:
                heapq.heappush(arr, element)

print(arr[0])
