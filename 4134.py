import sys
import math

t = int(sys.stdin.readline())


def isPrimeNum(n):
    i = 2
    while i * i <= n and i < math.sqrt(4 * 10 ** 9) + 1:
        if n % i == 0:
            return False
        i += 1
    return True


for i in range(t):
    num = int(sys.stdin.readline())
    if num == 0 or num == 1:
        print(2)
        break
    primeNum = num
    while primeNum >= num:
        if isPrimeNum(primeNum):
            print(primeNum)
            break
        else:
            primeNum += 1
