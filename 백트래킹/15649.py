import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
result = []
prev_elements = []
arr = [i for i in range(1, n + 1)]


def backTrack(elements):
    if len(prev_elements) == m:
        result.append(prev_elements[:])

    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)

        prev_elements.append(e)
        backTrack(prev_elements)
        prev_elements.pop()


backTrack(arr)
for i in result:
    for j in i:
        print(j, end=" ")
    print()
