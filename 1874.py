import sys

N = int(sys.stdin.readline())
arr = []
result = []
count = 1
possible = True
for i in range(N):
    num = int(sys.stdin.readline())
    while count <= num:
        arr.append(count)
        result.append("+")
        count += 1

    if arr[-1] == num:
        arr.pop()
        result.append("-")
    else:
        possible = False

if possible == False:
    print("NO")
else:
    for i in result:
        print(i)