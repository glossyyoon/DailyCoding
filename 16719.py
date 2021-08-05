import sys

s = list(sys.stdin.readline().rstrip())
li = [""] * len(s)


def solve(arr, start):
    if not arr:
        return
    minn = min(arr)
    idx = arr.index(minn)
    li[start + idx] = minn
    print("".join(li))
    solve(arr[idx + 1 :], start + idx + 1)
    solve(arr[:idx], start)


solve(s, 0)
