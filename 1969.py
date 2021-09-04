import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
newcleotyde = [0, 0, 0, 0]  # A, C, G, T

dna = []
result = ""
count = 0
for i in range(n):
    dna.append(sys.stdin.readline().rstrip())
for i in range(m):
    newcleotyde = [0, 0, 0, 0]  # A, C, G, T
    for j in range(n):
        if dna[j][i] == "A":
            newcleotyde[0] += 1
        elif dna[j][i] == "C":
            newcleotyde[1] += 1
        elif dna[j][i] == "G":
            newcleotyde[2] += 1
        elif dna[j][i] == "T":
            newcleotyde[3] += 1
    if newcleotyde.index(max(newcleotyde)) == 0:
        result += "A"
    elif newcleotyde.index(max(newcleotyde)) == 1:
        result += "C"
    elif newcleotyde.index(max(newcleotyde)) == 2:
        result += "G"
    elif newcleotyde.index(max(newcleotyde)) == 3:
        result += "T"

print(result)

for i in range(m):
    for j in range(n):
        if result[i] != dna[j][i]:
            count += 1
print(count)
