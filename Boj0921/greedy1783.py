n, m = map(int, input().split(' '))
check = []
count = 1
check.append([n-1, 0])
temp = [n-1, 0]
while(True):
    if temp[0]