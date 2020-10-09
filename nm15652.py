import sys
n, m = map(int, sys.stdin.readline().split(' '))
check = [0 for _ in range(n+1)]
result = [0 for _ in range(m)]
def permutation(start):
    if start == m:
        for i in result:
            print(i, end = ' ')
        print()
    else:
        for i in range(1, n+1):
            if check[i]==1:
                continue
            result[start] = i
            for j in range(i):
                check[j] = 1
            permutation(start+1)
            for k in range(n+1):
                check[k] = 0
permutation(0)