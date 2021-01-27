num = int(input())
array = [0, 1, 3, 5]
for i in range(4, 1001):
    array.append(array[i-2]*2+array[i-1])
print(array[num]%10007)