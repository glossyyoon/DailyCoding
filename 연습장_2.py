from itertools import combinations

n = "abcde"
a = list(combinations(range(1, len(n)), 2))
print(a)
for i in range(len(a)):
    q, p = a[i][0], a[i][1]
