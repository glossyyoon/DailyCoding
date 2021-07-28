import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a = [0] * 26
    s = input()
    for i in range(len(s)):
        if s[i].isalpha():
            num = ord(s[i]) - ord("a")
            a[num] += 1
    m = max(a)
    print(chr(ord("a") + a.index(m)) if a.count(m) < 2 else "?")
