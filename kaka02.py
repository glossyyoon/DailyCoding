import operator
 

def solution(orders, course):
    answer = []
    ords = []
    count = 0
    nums = []
    dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    for order in orders:
        ords.append([])
        for i in range(len(order)):
            ords[count].append(order[i:i+1])
        count+=1
    for i in ords:
        for j in i:
            if j=="A":
                dic['a']+=1
            elif j=="B":
                dic['b']+=1
            elif j=="C":
                dic['c']+=1
            elif j=="D":
                dic['d']+=1
            elif j=="E":
                dic['e']+=1
            elif j=="F":
                dic['f']+=1
            elif j=="G":
                dic['g']+=1
            elif j=="H":
                dic['h']+=1
            elif j=="I":
                dic['i']+=1
            elif j=="J":
                dic['j']+=1
            elif j=="K":
                dic['k']+=1
            elif j=="L":
                dic['l']+=1
            elif j=="M":
                dic['m']+=1
            elif j=="N":
                dic['n']+=1
            elif j=="O":
                dic['o']+=1
            elif j=="P":
                dic['p']+=1
            elif j=="Q":
                dic['q']+=1
            elif j=="R":
                dic['r']+=1
            elif j=="S":
                dic['s']+=1
            elif j=="T":
                dic['t']+=1
            elif j=="U":
                dic['u']+=1
            elif j=="V":
                dic['v']+=1
            elif j=="W":
                dic['w']+=1
            elif j=="X":
                dic['x']+=1
            elif j=="Y":
                dic['y']+=1
            elif j=="Z":
                dic['z']+=1
        sdict= sorted(dic.items(), key=operator.itemgetter(1))
        print(sdict)
        for j in course:
            for k in range(j):
                all_values = dic.values()
                max_value = max(all_values)
                answer.append(k for k, v in dic.items() if v == 'max_value')
                
    return answer
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))