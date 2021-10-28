from collections import deque


def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = (
                    min(board[i - 1][j - 1], board[i][j - 1], board[i - 1][j]) + 1
                )
    return max([item for r in board for item in r]) ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
