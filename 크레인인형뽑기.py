def solution(board, moves):
    answer = []
    result = 0
    flag = False
    # 30*30*1000 < 10**8
    for m in moves:
        m -= 1
        flag = False
        for i in range(len(board)):
            if flag:
                break
            for j in range(len(board)):
                if m==j and board[i][m]!=0:
                    if len(answer)>0 and answer[-1]==board[i][m]:
                        answer.pop()
                        result += 2
                        board[i][m] = 0
                        if len(answer)>1 and answer[-1]==answer[-2]:
                            answer.pop()
                            answer.pop()
                            result += 2
                        flag = True
                        break
                    else:
                        answer.append(board[i][m])
                        board[i][m] = 0
                        flag = True 
                        break       
    return result