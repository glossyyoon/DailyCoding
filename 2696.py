import sys

n = int(input())
for i in range(n):
    m = int(input())
    li = []
    for i in range(m // 10 + 1):
        li += list(map(int, input().split()))
    print(m // 2 + 1)
    print(li[0], end=" ")
    for i in range(2, m, 2):
        arr = sorted(li[: i + 1])
        print(arr[i // 2], end=" ")
    print()
