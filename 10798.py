li = [[] for _ in range(15)]
for _ in range(5):
    l = list(input())
    for i in range(len(l)):
        li[i] += l[i]
for i in li:
    for j in i:
        print(j, end="")
