num1 = int(input())
empty = num1
for i in range(1, num1+1):
    print(' '*(empty-i)+'*'*i)
for k in range(1, num1+1):
    print(' '*k+'*'*(num1-k))