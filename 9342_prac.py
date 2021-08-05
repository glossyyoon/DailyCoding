import sys

n = int(sys.stdin.readline())
must = "ABCDEF"


def solution(g):
    if g[0] != "A":
        g = g[1:]
    idx = 0
    if g[idx] == "A":
        idx += 1
        while g[idx] == "A":
            idx += 1
        if g[idx] == "F":
            idx += 1
            while g[idx] == "F":
                idx += 1
            if g[idx] == "C":
                while idx < len(g) and g[idx] == "C":
                    idx += 1
                if idx == len(g):
                    return True
                elif idx == len(g) - 1 and g[idx] in must:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


for i in range(n):
    gene = sys.stdin.readline().rstrip()
    if solution(gene):
        print("Infected!")
    else:
        print("Good")
