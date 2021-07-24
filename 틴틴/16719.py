import sys

input = sys.stdin.readline
s = list(input().rstrip())
result = [""] * len(s)


def func(arr, start):
    if not arr:
        return
    minn = min(arr)
    idx = arr.index(minn)
    result[start + idx] = minn
    print("".join(result))
    func(arr[idx + 1 :], start + idx + 1)
    func(arr[:idx], start)


func(s, 0)
