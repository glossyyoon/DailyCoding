n = int(input())
for k in range(n):
    v = int(input())
    cnt = 0
    for i in range(v):
        if i == 1:
            continue
        if len([1 for z in [j for j in range(2, i)] if i % z == 0]) == 0:
            cnt += 1

    print(cnt)
