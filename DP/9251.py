import sys

s1 = list(sys.stdin.readline().rstrip())
s2 = list(sys.stdin.readline().rstrip())
lcs = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
maximum = 0
for i in lcs:
    for j in i:
        if int(j) > maximum:
            maximum = int(j)
print(maximum)
