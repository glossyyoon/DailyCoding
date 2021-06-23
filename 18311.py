n, k = map(int, input().split())
l = [0 for _ in range(100000)]
course = list(map(int, input().split()))
add = 0
count = [i for i in range(1, n + 1)]
temp = 0
q = 0
w = 0

for i in range(5):
    add += course[i]


def findCourse(k, q):
    global course, count, l, temp
    for i in range(q, n + q):
        for j in range(temp, course[i] + temp):
            l[j] = count[i]
            temp += 1
        q += 1


while temp <= k:
    findCourse(k, q)
    course = [course[-1]] + course[-2::-1]
    count = [count[-1]] + count[-2::-1]
print(l[k])