class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(r, c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            return

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count