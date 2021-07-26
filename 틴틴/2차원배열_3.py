l = [[10, 20], [30, 40], [50, 60]]
i = 0
while i < len(l):
    x, y = l[i]
    print(x, y)
    i += 1

while i < len(l):
    x, y = l[i][0], l[i][1]
    print(x, y)
    i += 1
