import sys
n, m = map(int, sys.stdin.readline().split())
check = [0 for _ in range(n+1)]
result = [0 for _ in range(m)]
def permutation(index, n):
    if index==m:
        for i in range(n):
            print(result[i], end = ' ')
        print()
    else:
        for i in range(1, n+1):
            if check[i]==1:
                continue
            check[i]=1
            result[index]=i
            permutation(index+1, n)
            check[i] = 0
permutation(0, n)