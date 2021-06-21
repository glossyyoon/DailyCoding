arr = list(map(int, input().split(",")))
result = []


def solution(arr):
    setArr = set(arr)
    for i in setArr:
        countOf(i)
    sorted(result)
    if result == []:
        return [-1]
    else:
        return result


def countOf(e):
    count = 0
    for i in range(len(arr)):
        if e == arr[i]:
            count += 1
    if count != 1:
        result.append(count)


print(solution(arr))
#1, 2, 3, 3, 3, 3, 4, 4