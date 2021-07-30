import sys

s, b = sys.stdin.readline().split()
newAlpha = [chr(ord("A") + i) for i in range(int(b) - 10)]
result = 0
count = 0
for i in range(len(s) - 1, -1, -1):
    count += 1
    a = s[i]
    if a.isalpha():
        idx = newAlpha.index(a)
        idx += 10
    else:
        idx = a

    result += int(idx) * int(b) ** (count - 1)
print(result)
