num1 = input()
length = len(num1)
for i in range(0, length+1, 10):
    print(num1[i:i+10])