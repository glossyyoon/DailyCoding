def solution(k, score):
    answer = -1
    diff = [0]
    for i in range(len(score)-1):
        diff.append(abs(score[i+1]-score[i]))
    comp = {}
    for q in range(len(diff)):
        if diff[q] in comp.keys():
            comp[diff[q]] +=1
        else:
            comp[diff[q]] = 1
    nums = []
    result = 1
    for y in comp:
        if comp[y]>=k:
            nums.append(y)
            if y == diff[1]:
                result = 0
    for l in nums:
        del comp[l]
    answer = len(comp)-1-result
    print(answer)
    return answer
solution(3, [24,22,20,10,5,3,2,1])
solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100])