from itertools import combinations

n = int(input())


def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)


for i in range(n):
    result = []
    r = 0
    num, *arr = map(int, input().split())
    c = list(combinations(arr, 2))
    for j in range(len(c)):
        n, m = c[j][0], c[j][1]
        result.append(gcd(n, m))
    for k in result:
        r += k
    print(r)
