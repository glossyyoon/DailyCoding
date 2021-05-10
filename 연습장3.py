num = int(input())


def nine(num):
    a = 1
    while a != 10:
        print(num, "*", a, "=", num * a)
        a += 1


nine(num)