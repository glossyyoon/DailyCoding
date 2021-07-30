import sys

n = sys.stdin.readline()


def cycle(l, r):
    new = str(int(l) + int(r))
    return r + new[-1]


count = 1

if len(n) == 2:
    left = "0"
    right = n[0]
else:
    left, right = n[0], n[1]

while True:
    newStr = cycle(left, right)
    if int(newStr) == int(n):
        print(count)
        break
    else:
        left, right = newStr[0], newStr[1]
        count += 1
        continue
