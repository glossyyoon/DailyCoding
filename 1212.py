num = input()
newNum = 0
newBNum = 0
for i in range(len(num)):
    newNum += int(num[abs(len(num) - (i + 1))]) * (8**i)
while True:
    if newNum == 1:
        break
    newNum //= 2
    newBNum = str(newNum % 2) + str(newBNum)

print(newBNum)