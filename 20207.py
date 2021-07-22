n = int(input())
calendar = [0] * 367
max_day = 0
result = []
for i in range(n):
    s, e = map(int, input().split())
    if max_day < e:
        max_day = e
    for j in range(s, e + 1):
        calendar[j] += 1

count = 0
m = 0
for k in range(max_day + 2):
    if calendar[k] == 0 or k == max_day + 1:
        result.append(count * m)
        count = 0
        m = 0
        continue
    else:
        if m < calendar[k]:
            m = calendar[k]
        count += 1
r = 0
for i in result:
    r += i
print(r)
