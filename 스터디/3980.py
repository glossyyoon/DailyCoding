import sys

T = int(sys.stdin.readline().rstrip())

def solution(idx, curr_sum):
    global max_sum
    if idx==11:
        if curr_sum>max_sum:
            max_sum = curr_sum
            return
    for j in range(11):
        if visit[j]:
            continue
        if player[idx][j] != 0:
            visit[j] = True
            solution(idx+1, curr_sum + player[idx][j])
            visit[j] = False

for i in range(T):
    player = []
    for i in range(11):
        h = list(map(int, sys.stdin.readline().rstrip().split()))
        player.append(h)
    visit = [False]*11
    max_sum = 0
    solution(0,0)
    print(max_sum)