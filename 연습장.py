date = input()
year, month, day = map(int, date.split('.'))
print("%d.%02d.%02d" % (year, month, day))