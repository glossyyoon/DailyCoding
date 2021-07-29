t = int(input())
must = "ABCDEF"
for i in range(t):
    dna = input()
    count = 0
    idx = 1
    if not dna[0] in must:
        idx = 0

    for j in range(idx, len(dna)):
        if count == 0 and dna[j] == "A":
            continue
        if count == 0 and dna[j] == "F":
            count += 1
            continue
        if count == 1 and dna[j] == "C":
            count += 1
            continue
        if count == 2 and dna[j] in must and j == len(dna) - 1:
            print("Infected!")
            break
        else:
            print("Good")
            break
