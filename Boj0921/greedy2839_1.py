import sys
sugar = int(sys.stdin.readline())
bags = 0
while(True):
    if sugar%5==0:
        bags += sugar//5
        print(bags)
        break
    sugar -=3
    bags +=1
    if sugar <0:
        print(-1)
        break