# num = int(input())
# l = []
# result = []

# def find(word):
#     global result
#     for i in range(len(result)):
#         if word == result[i][0]:
#             result[i][1] += 1
#             break
#         else:
#             result.append([word, 1])
#             break

# for i in range(num):
#     l.append(list(input().split(".")))

# result.append([l[0][1], 1])

# for k in range(1, num):
#     find(l[k][1])
# print(result)
import sys
input = sys.stdin.readline

n = int(input())
file = dict()
for i in range(n):
    extend = (input().split("."))[1]
    if not extend in file:
        file[extend] = 1
    else:
        file[extend] += 1
sort_file = sorted(file.items())
for key, value in sort_file:
    print(key.rstrip(), value)