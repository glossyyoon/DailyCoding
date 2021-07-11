import sys
from itertools import combinations

func = list(sys.stdin.readline())
p, prob_idx = [], []
for idx, i in enumerate(func):  #괄호가 있던 위치를 저장하고 괄호를 빈 문자열로 바꾸기
    if i == "(":
        func[idx] = ""
        p += [idx]
    elif i == ")":
        func[idx] = ""
        prob_idx += [[p.pop(), idx]]
stack = []
for i in range(len(prob_idx)):
    for j in combinations(prob_idx, i):  #수열 조합을 만들어주는 combinations함수를 사용
        F = func[:]
        for v, w in j:
            F[v] = "("
            F[w] = ")"
        stack.append("".join(F))
stack = set(stack)
stack = sorted(stack)

for i in stack:
    print(i, end="")