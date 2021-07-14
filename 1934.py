import sys
import math

n = int(sys.stdin.readline())
stack = 1
count = 2
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    q, w = a, b
    if math.gcd(q, w) == 1:
        print(q * w)
        continue
    while math.gcd(q, w) != 1:
        if q % count == 0 and w % count == 0:
            q //= count
            w //= count
            stack *= count
            count += 1
        count += 1
    print(stack * q * w)
    stack = 0
