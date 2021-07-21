n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    print(arr[i - 1] - arr[i])
