n = int(input())
candy = []
while n != 0:
    candy.append(list(map(str, input())))
    n -= 1
print(candy)