import sys
n = input()
while True:
    if n=="END":
      sys.exit(0)
    print(n[::-1])
    n = input()
