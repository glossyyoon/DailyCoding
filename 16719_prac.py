s = list(input())
r = [""] * len(s)


def func(arr, start):
    if not arr:
        return
    minn = min(arr)
    idx = arr.index(minn)
    r[start + idx] = minn
    print("".join(r))
    func(arr[idx + 1 :], start + idx + 1)
    func(arr[:idx], start)


func(s, 0)
