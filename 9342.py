import sys

t = int(sys.stdin.readline())


def solution():
    must = "ABCDEF"
    dna = sys.stdin.readline().rstrip()
    if len(dna) <= 2:
        print("Good")
        return
    if dna[0] not in must:
        print("Good")
        return
    if dna[-1] not in must:
        print("Good")
        return

    if dna[0] != "A":
        dna = dna[1:]

    idx = 0
    stage = 1
    while idx < len(dna):
        if stage == 1:
            if dna[idx] != "A":
                print("Good")
                return
            else:
                stage = 2

        elif stage == 2:
            if dna[idx] == "A":
                stage = 2
            elif dna[idx] != "F":
                print("Good")
                return
            else:
                stage = 3

        elif stage == 3:
            if dna[idx] == "F":
                stage = 3
            elif dna[idx] != "C":
                print("Good")
                return
            else:
                stage = 4

        elif stage == 4:
            if dna[idx] == "C":
                stage = 4
            else:
                stage = 5

        else:
            print("Good")
            return

        idx += 1
    print("Infected!")


while t > 0:
    solution()
    t -= 1
