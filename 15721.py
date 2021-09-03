a = int(input())
t = int(input())
bun = int(input())
n = 0
person = 0
num = 2
if bun == 0:
    for i in range(1, 10000):
        if n == t:
            print(person)
            break
        person += 1
        n += 1
        person += 2
        n += 1
        for j in range(1, num + 1):
            person += 1
            n += 1
        num += 1
