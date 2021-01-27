arr = [1, 2, 4]
num = int(input())
count = 0
while count!=num:
    i = int(input())
    for j in range(3, 11):
        arr.append(arr[j-1]+arr[j-2]+arr[j-3])
    print(arr[i-1])
    count += 1