e, s, m = map(int, input().split())
e -= 1
s -= 1
m -= 1
year = 0
while True:
    if year % 15 == e and year % 25 == 0 and year % 19 == 0:
        print(year + 1)
        break
    year += 1