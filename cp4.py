count = 0
def solution(depar, hub, dest, roads):
    answer = -1
    rods = {}
    for i in range(len(roads)):
        temp = roads[i][0]
        if temp in rods.keys():
            rods[temp] = [rods[temp], roads[i][1]]
        else:
            rods[temp] = roads[i][1]
    check = [[]]
    for j in rods.keys():
        check.append(j)
    def recur(start):
        check[start] = 1
        for e in rods[start]:
            if check[e][1]==0:
                recur(e)
        answer+=1
    recur(depar)
    print(answer)
    return answer
solution("SEOUL","DAEGU","YEOSU",[["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]])