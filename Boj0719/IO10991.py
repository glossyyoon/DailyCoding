# num1 = int(input())
# for i in range(1, 2*num1):
#     empty = num1-i
#     if i%2==1:
#         print(" "*empty)
#         count = 1
#         while(count != num1):
#             for k in range(1, count+1):
#                 print("*"+" ",end=' ')
#             count+=1
#     else:
#         print()
num1 = int(input())
num2 = num1
for i in range(num1):
    print(" "*(num2-i-1)+'*'+' *'*i)