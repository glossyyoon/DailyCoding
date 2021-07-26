# [[0, 0], [0, 0], [0, 0]]
a = []
for i in range(3):
    b = []
    for j in range(2):
        b.append(0)
    a.append(b)
print(a)


b = [[0 for i in range(2)] for j in range(3)]
print(b)
