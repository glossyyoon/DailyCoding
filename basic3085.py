# def check(a):
#     n = len(a)
#     for i in range(n):
#         for j in range(n):

# n = int(input())
# a = [list(input()) for _ in range(n)]
# ans = 0
# for i in range(n):
#     for j in range(n):
#         if j+1<n:
#             a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
#             temp = check(a)
#             if ans<temp:
#                 ans = temp
#             a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
