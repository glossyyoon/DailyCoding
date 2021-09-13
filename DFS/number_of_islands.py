class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return
            grid[i][j] = 0

            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for k in range(4):
                dfs(i + dx[k], j + dy[k])

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
