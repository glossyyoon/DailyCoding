import sys

n, k = map(int, sys.stdin.readline().split())
course = list(map(int, sys.stdin.readline().split()))
l = []
count = [i for i in range(1, n + 1)]
temp = 0
q = 0

while True:
    course += course[-1::-1]
    count += count[-1::-1]
    for i in range(q, n + q - 1):
        for j in range(temp, course[i] + temp):
            if j == k:
                print(l[-1])
                sys.exit()
            l.insert(j, count[i])
            temp += 1
        q += 1
