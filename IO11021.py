num = int(input())
for i in range(num):
    num1, num2 = map(int, input().split())
    print("Case #%d: %d"%(i+1,num1+num2))