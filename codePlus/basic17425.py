MAX = 1000000
d = [1] * (MAX + 1)
s = [0] * (MAX + 1)
for i in range(2, MAX + 1):
    j = 1
    while i * j <= MAX:
        d[i * j] += i
        j += 1
for i in range(1, MAX + 1):
    s[i] = s[i - 1] + d[i]
ans = []
n = int(input())
for _ in range(n):
    t = int(input())
    ans.append(s[t])
print('\n'.join(map(str, ans)) + '\n')
