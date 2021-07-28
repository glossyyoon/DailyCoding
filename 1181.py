import sys

input = sys.stdin.readline
n = int(input())
result = []
for i in range(n):
    w = str(input())
    w_count = len(w)
    result.append((w, w_count))
result = list(set(result))
result.sort(key=lambda word: (word[1], word[0]))
print(result)
# for w in result:
#     print(w[0], end="")
