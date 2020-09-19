import sys
num = int(sys.stdin.readline())
def five(num_in):
    five = num//5
    three = 0
    if five%3 ==0 or five%5==0:
        three = (num%5)//3
        print(five+num)
    else:
        threes(num_in)
    
def threes(num_in):
    three = num_in//3
    if num_in%3!=0:
        print(-1)
    else:
        print(three)
five(num)