import sys

h2, m2, s2 = map(int, sys.stdin.readline().split(":"))
h1, m1, s1 = map(int, sys.stdin.readline().split(":"))

h = m = s = 0
if s1 < s2:
    m1 -= 1
    s1 += 60
s = s1 - s2
if len(str(s)) == 1:
    s = "0" + str(s)
if m1 < m2:
    h1 -= 1
    m1 += 60
m = m1 - m2
if len(str(m)) == 1:
    m = "0" + str(m)
if h1 < h2:
    h2 = 24 - h2
    h = h1 + h2
else:
    h = h1 - h2
if len(str(h)) == 1:
    h = "0" + str(h)
if h == "00" and m == "00" and s == "00":
    print("24:00:00")
    exit(0)
else:
    print(f"{h}:{m}:{s}")
