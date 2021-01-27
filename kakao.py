# def solution(v):
#     answer = []
#     for i in range(1):
#         if v[i][0]==v[i+1][0] and v[i][0]!=v[i+2][0]:
#             num = max(v[i][1], v[i+1][1])
#             num2 = min(v[i][1], v[i+1][1])
#             if v[i+2][1]==num:
#                 answer=([v[i+2][0], num2])
#             else:
#                 answer=([v[i+2][0], num])
#         elif v[i][0]!=v[i+1][0] and v[i+1][0]==v[i+2][0]:
#             num = max(v[i+1][1], v[i+2][1])
#             num2 = min(v[i+1][1], v[i+2][1])
#             if v[i][1]==num:
#                 answer =([v[i][0], num2])
#             else:
#                 answer=([v[i][0], num])
#         elif v[i][0]==v[i+2][0] and v[i][0]!=v[i+1][0]:
#             num = max(v[i][1], v[i+2][1])
#             num2 = min(v[i][1], v[i+2][1])
#             if v[i+1][0]==num:
#                 answer = (v[i+1][0], num2)
#             else:
#                 answer=([v[i+1][0], num])
#     return answer

def solution(v):
    answer = []
    answer = (v[0][0]^v[1][0]^v[2][0], v[0][1]^v[1][1]^v[2][1])
    
    return answer
print(solution([[1, 4], [3, 4], [3, 10]]))