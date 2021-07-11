import sys
from itertools import combinations

func = list(sys.stdin.readline())
tmp, stack = [], []
result = []
for idx, i in enumerate(func):
    if i == "(":
        tmp.append(idx)
        func[idx] = ""
    elif i == ")":
        t = tmp.pop()
        stack.append([t, idx])
        func[idx] = ""
for i in range(len(stack)):
    p, q = 0, 0
    for j in combinations(stack, i):
        F = func[:]
        for a, b in j:
            F[a] = "("
            F[b] = ")"
        result.append("".join(F))
result = set(result)
result = sorted(result)
for i in result:
    print(i, end="")
