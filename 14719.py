import sys

input = sys.stdin.readline
maxH = 1
maxL = 0
H, W = map(int, input().split())
rain = list(map(int, input().split()))

for i in range(len(rain)):
    if maxH < rain[i]:
        maxH = rain[i]
        maxIdx = i
total = 0
temp = 0
for i in range(maxIdx + 1):
    if temp < rain[i]:
        temp = rain[i]
    total += temp
temp = 0
for i in range(W - 1, maxIdx, -1):
    if temp < rain[i]:
        temp = rain[i]
    total += temp
print(total - sum(rain))
