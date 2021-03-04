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
#   1 def dfs(graph, start_node):
#   2     visit = list()
#   3     stack = list()
#   4
#   5     stack.append(start_node)
#   6
#   7     while stack:
#   8         node = stack.pop()
#   9         if node not in visit:
#  10             visit.append(node)
#  11             stack.extend(graph[node])
#  12
#  13     return visit