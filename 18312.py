n, k = map(int, input().split())
count = 0
for i in range(n + 1):
    if len(str(i)) == 1:
        i = str(0) + str(i)
    if i == 0:
        i = "00"
    for j in range(60):
        if len(str(j)) == 1:
            j = str(0) + str(j)
        if j == 0:
            j = "00"
        for p in range(60):
            if len(str(p)) == 1:
                p = str(0) + str(p)
            if p == 0:
                p = "00"
            if str(k) in str(i) + str(j) + str(p):
                count += 1
print(count)
