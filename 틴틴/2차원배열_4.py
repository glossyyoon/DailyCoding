l = [[10, 20], [30, 40], [50, 60]]
i = 0
while i < len(l):
    j = 0
    while j < len(l[i]):
        print(l[i][j], end=" ")
        j += 1
    print()
    i += 1
