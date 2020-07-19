num1 = int(input())
empty = 0
for i in range(1, num1+1):
    empty = num1-i
    print(" "*empty+"*"*i)
for j in range(num1-1, 0, -1):
    empty = num1-j
    print(" "*empty+"*"*j)