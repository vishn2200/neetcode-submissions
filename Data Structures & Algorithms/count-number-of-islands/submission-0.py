class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i,j):
            visited[i][j] = True
            if j+1 < cols and not visited[i][j+1] and grid[i][j+1] == "1":
                dfs(i,j+1)
            if i+1 < rows and not visited[i+1][j] and grid[i+1][j] == "1" :
                dfs(i+1,j)
            if j-1 >=0 and not visited[i][j-1] and grid[i][j-1] == "1":
                dfs(i,j-1)
            if i-1 >=0 and not visited[i-1][j] and grid[i-1][j] == "1":
                dfs(i-1,j)

            return
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    res+=1
                    dfs(i,j)
        return res
            