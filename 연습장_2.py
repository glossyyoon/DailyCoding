def isPrimeNum(num):
    n = 2
    if num == 2 or num == 3:
        return True
    while n != num:
        if num % n == 0:
            return False
        else:
            n += 1
            num
    return True


print(isPrimeNum(5))
