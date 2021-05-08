n = input()
l = len(n)
ans = 0
k = 1
ten = 1
while k != l:
    ans += (9 * k) * ten
    k += 1
    ten *= 10
if k == l:
    ans += (int(n) - ten + 1) * k
print(ans)