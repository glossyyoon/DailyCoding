while(True):
    num1, num2 = map(int, input().split())
    if (num1==0 & num2==0 ):
        exit()
    else:
        print(num1 + num2)