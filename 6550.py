# while True:
s, t = input().split()
idx = 0
sIdx = 0
flag = False
while idx < len(t):
    newarr = t[idx:]
    for i in range(len(newarr)):
        if s[sIdx] == newarr[i]:
            idx = i
            print(i)
            sIdx += 1
            break
        else:
            flag = False
            break
        break
if sIdx == len(s):
    flag = True
if flag == False:
    print("No")
    # break
else:
    print("Yes")
    # break
print("Yes")
