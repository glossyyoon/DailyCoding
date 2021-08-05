import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    s = sys.stdin.readline().rstrip()
    arr.append((s, len(s)))
arr = list(set(arr))
arr.sort(key=lambda word: (word[1], word[0]))
for i in arr:
    print(i[0])
