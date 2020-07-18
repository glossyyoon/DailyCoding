month, day = map(int, input().split(" "))
result = 0
dayList = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i in range(month):
    result+=dayList[i]
print(weekList[(result+day)%7])