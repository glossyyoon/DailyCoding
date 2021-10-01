# 지윤
def solution(weights, head2head):
    player = []
    for idx, l in enumerate(head2head):
        possibility = 0
        length = len(l)
        w_count = 0
        for i, game in enumerate(l):
            if game == "W":
                possibility += 1
                if weights[idx] < weights[i]:
                    w_count += 1
            elif game == "N":
                length -= 1
        if length == 0:
            player.append([0, w_count, weights[idx], idx])
        else:
            player.append([possibility / length, w_count, weights[idx], idx])

    player = sorted(player, key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    answer = list(player[i][3] + 1 for i in range(len(weights)))
    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
