# 원하는 답은 얻을 수 있지만 굉장히 비효율적인 풀이이다.
import sys
# num = int(sys.stdin.readline())
# meetings = []
# counts = []
# count = [1 for _ in range(num)]
# for i in range(num):
#     n, m = map(int, sys.stdin.readline().split(' '))
#     meetings.append([n, m])

# def rec(start):
#     count[j] +=1
#     for k in range(start+1, num-1):
#         if meetings[k][0]>=meetings[start][1]:
#             rec(k)
#             break

# for j in range(num):
#     rec(j)
#     counts.append(count[j])
# print(max(counts))
num = int(sys.stdin.readline())
s = []
meeting = []
last = 0
count = 0
for i in range(num):
    n, m = map(int, sys.stdin.readline().split(' '))
    s.append([n,m])
meeting = sorted(s, key = lambda x: [x[1], x[0]])
for i, j in meeting:
    if i>=last:
        count+=1
        last = j
print(count)