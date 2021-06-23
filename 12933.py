sound = input()
visited = [False] * len(sound)
count = 0
if len(sound) % 5 != 0:
    print(-1)
    exit()


def solve(start):
    global count
    quack = 'quack'
    first = True
    j = 0
    for i in range(start, len(sound)):
        if sound[i] == quack[j] and not visited[i]:
            visited[i] = True
            if sound[i] == 'k':
                if first:
                    count += 1
                    first = False
                j = 0
                continue
            j += 1


for i in range(len(sound)):
    if sound[i] == 'q' and not visited[i]:
        solve(i)
if not all(visited) or count == 0:
    print(-1)
else:
    print(count)
