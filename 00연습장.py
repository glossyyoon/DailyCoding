def solution(begin, target, words):
    global visited, count
    visited = [False] * len(words)
    count = 0

    def dfs(curr):
        global count, visited
        if curr == target:
            return answer
        for i in range(len(target)):
            for j in range(len(words)):
                if visited[j] == False:
                    if curr[:i] + curr[i + 1 :] == words[j][:i] + words[j][i + 1 :]:
                        visited = True
                        count += 1
                        dfs(words[j])
                        visited = False

    dfs(begin)
    print(visited)
    return count


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
