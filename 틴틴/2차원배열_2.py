l = [[10, 20], [30, 40], [50, 60]]
# range대신 in을 써서
for i in l:
    for j in i:
        print(j, end=" ")
    print()

for i, j in l:
    print(i, j)
