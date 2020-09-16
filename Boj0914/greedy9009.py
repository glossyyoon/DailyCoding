import sys
n= int(sys.stdin.readline())
fibo = [0, 1, 1, 2]
while fibo[-1] < 1000000000:
    fibo.append(fibo[-1]+fibo[-2])
for _ in range(n):
    result = []
    num = int(sys.stdin.readline())
    while num>0:

        for i in range(len(fibo)-1, 0, -1):
            if fibo[i]<=num:
                temp = fibo[i]
                result.append(temp)
                num = num-fibo[i]
        result.sort()
    for b in range(len(result)):
        print(result[b], end = ' ')
    print()
# p = [1,2]
# for i in range(2, 46):
#     p.append(p[i-2]+p[i-1]) 
# T = int(input())

# for j in range(T):
#     n = int(input())
#     result=[]
#     while(n):
#         for k in range(46):
#             if(p[k]<=n):
#                 t = p[k]
#         n -= t
#         result.append(t)
#         result.sort()
#     for b in range(len(result)):
#         print(result[b], end=' ')