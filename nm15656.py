import sys
n, m = map(int, sys.stdin.readline().split(' '))
num = list(map(int, sys.stdin.readline().split(' ')))
check = [0 for _ in range(max(num)+1)]
result = [0 for _ in range(m)]
num.sort()
def permutation(start):
    if start==m:
        for i in result:
            print(i, end = ' ')
        print()
    else:
        for i in num:
            if check[i]==1:
                continue
            result[start] = i
            permutation(start+1)
permutation(0)