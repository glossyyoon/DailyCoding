import sys

N, K = map(int, sys.stdin.readline().split())
circle = [i for i in range(N)]
result = []

popNum = 0

while circle:
    popNum = (popNum + K - 1) % len(circle)
    result.append(str(circle.pop(popNum) + 1))
print("<%s>" % (", ").join(result))
