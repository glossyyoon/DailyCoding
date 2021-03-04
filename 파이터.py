def main():
    skill = input().split()
    relation = int(input())
    visit = [False] * relation
    graph = {string: [] for string in skill}
    for i in range(relation):
        x, y = input().split()
        graph[x].append(y)

    def dfs(graph, start_node):
        visit = list()
        stack = list()
        stack.append(start_node)
        while stack:
            node = stack.pop()
            if node not in visit:
                visit.append(node)
                stack.extend(graph[node])
        return visit

    print(dfs(graph, skill[0]))


if __name__ == "__main__":
    main()