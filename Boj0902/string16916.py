def out():
    S = list(str(input()))
    P = list(str(input()))
    if S != [] and P!=[] and len(S)<1000001 or len(P)<1000001:
        start = 0
        result = []
        for i in range(len(S)):
            for j in range(len(P)):
                if start == 0 and P[j]==S[i]:
                    result.append(P[j])
                    start = 1
                    i+=1
                    j+=1
                    while(True):
                        try:
                            if result==P:
                                return 1

                            elif start==1 and S[i]!=P[j]:
                                return 0

                            elif start==1 and S[i]==P[j]:
                                result.append(P[j])
                                i+=1
                                j+=1
                        except:
                            return 0
                elif i==len(S)-1 and j==len(P)-1:
                    return 0

print(out())