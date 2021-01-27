num1 = int(input())
num2 = num1
for i in range(num1-1):
    if i!=0:
        print(" "*(num2-i-1)+'*'+' '*(i*2-1)+"*")
    else:
        print(" "*(num2-i-1)+'*'+' '*(i*2-1))
print("*"*(num2*2-1))