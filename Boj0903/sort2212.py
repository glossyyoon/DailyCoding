n = int(input())
k = int(input())
if k>=n:
    print(0)
    exit()
distance = []
arr = list(map(int, input().split(' ')))
arr.sort()
for i in range(1, n):
    distance.append(arr[i] - arr[i-1]) 
distance.sort(reverse = True)
for i in range(k-1):
    distance[i] = 0
print(sum(distance))

