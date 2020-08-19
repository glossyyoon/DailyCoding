num = int(input())
arr = [0, 0, 1, 1, 2]

for i in range(5, num+1):
    case1 = arr[i-1] + 1
    if i%2 == 0:
        case2 = arr[i//2]+1
        case1 = min(case1, case2)
    if i%3 == 0:
        case3 = arr[i//3]+1
        case1 = min(case1, case3)
    arr.append(case1)
print(arr[num])
