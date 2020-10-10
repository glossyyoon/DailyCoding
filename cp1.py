def solution(N):
    temp = N
    arr = []
    answer = []
    ans = []
    num = 1
    for i in range(2, 10):
        temp = N
        y=""
        while(temp>0):
            y+=str(temp%i)
            temp = temp//i
        arr.append(y)

    for j in arr:
        string = 1
        for l in range(len(j)):
            if int(j[l:l+1])!= 0:
                string *= int(j[l:l+1])
        ans.append(string)
    print(ans)
    maxnum = 0
    index = 0
    for k in range(len(ans)):
        if ans[k]>maxnum:
            maxnum = ans[k]
            index = k
        elif ans[k]==maxnum and k>index:
            index = k

            
    answer.append(index+2)
    answer.append(maxnum)
    return answer
print(solution(14))