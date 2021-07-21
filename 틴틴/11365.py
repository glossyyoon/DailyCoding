import sys

n = input()
while True:
    if n == "END":
        break
    print(n[::-1])
    n = input()
