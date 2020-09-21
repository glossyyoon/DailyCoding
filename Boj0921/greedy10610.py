n = list(input())
num = 0
count = 0
n.sort(reverse = True)
for i in range(len(n)):
    num += int(n[i])
    if n[i]=='0':
        count += 1
if num%3!= 0 or count==0:
    print(-1)
else:
    for i in range(len(n)):
        print(n[i], end = '')