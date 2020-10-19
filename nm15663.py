import sys
n, m = map(int, sys.stdin.readline().split(' '))
num = list(map(int, sys.stdin.readline().split(' ')))
num.insert(0, 0)
check = [0 for _ in range(len(num))]
result = [0 for _ in range(m)]
num.sort()
arr = []
def permutation(start):
    if start==m:
        arr.append(result)
        for i in result:
            print(i, end = ' ')
        print()
    else:
        overlap = 0
        for i in range(1, n+1):
            if check[i]==1:
                continue
            if overlap!=num[i]:
                check[i] = 1
                result[start] = num[i]
                overlap = num[i]
                permutation(start+1)
                check[i] = 0
    
permutation(0)