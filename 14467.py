num = int(input())
cows = []
count = 0


def isItCrossed(cow, road):
    global count
    if len(cows) != 0:
        for i in range(len(cows)):
            if cows[i][0] == cow and cows[i][1] != road:
                cows[i][1] = road
                count += 1
                break
            elif cows[i][0] == cow and cows[i][1] == road:
                break
            else:
                cows.append([cow, road])
    elif len(cows) == 0:
        cows.append([cow, road])


for i in range(num):
    cow, road = map(int, input().split())
    isItCrossed(cow, road)

print(count)