23 2 21 4 11 
6 18 17 12 10 
25 19 13 7 1 
16 14 9 8 20 
15 22 5 24 3 


for i in range(n + 1):  # 주대각선
    prev_list.append(graph[i][i])

for i in range(n + 1):  # 주대각선 -> 가운데행
    prev_temp = graph[(n + 1) // 2][i]
    graph[(n + 1) // 2][i] = prev_list[i]
    prev_list[i] = prev_temp

for i in range(n + 1):  # 가운데행 -> 부대각선
    prev_temp = graph[n - i][i]
    graph[n - i][i] = prev_list[i]
    prev_list[i] = prev_temp

for i in range(n + 1):  # 부대각선 -> 가운데열
    prev_temp = graph[n - i][(n + 1) // 2]
    graph[n - i][(n + 1) // 2] = prev_list[i]
    prev_list[i] = prev_temp

for i in range(n + 1):  # 가운대열 -> 주대각선
    graph[n - i][n - i] = prev_list[i]