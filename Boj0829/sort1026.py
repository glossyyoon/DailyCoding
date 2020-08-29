num = int(input())
result = 0
A = list(map(int, input().split(" ")))
A.sort()
B = []
for b in range(len(A)-1, -1, -1):
    B.append(A[b])
for i in range(num):
    result += A[i]*B[i]
print(A)
print(B)
print(result)
