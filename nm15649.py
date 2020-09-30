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
            check[i] = 1
            result[start] = i
            permutation(start+1)
            check[i] = 0
permutation(0)