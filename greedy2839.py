import sys
num = int(sys.stdin.readline())
box = 0
while True:
    if num%5==0:
        box  = box + num//5
        print(box)
        break
    num = num-3
    box+=1
    if num<0:
        print(-1)
        break


# inp = int(input())
# Box = 0
# while True:
#     if (inp % 5) == 0:
#         Box = Box + (inp//5)
#         print(Box)
#         break
#     inp = inp-3
#     Box += 1
#     if inp < 0:
#         print("-1")
#         break