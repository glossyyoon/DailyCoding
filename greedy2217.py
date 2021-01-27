import sys
num = int(sys.stdin.readline())
arr = []
result = []
if num>=1 and num<=100000:
    for i in range(num):
        arr.append(int(input()))
    arr.sort(reverse=True)
    for i in range(num):
        result.append(arr[i]*(i+1))
print(max(result))
