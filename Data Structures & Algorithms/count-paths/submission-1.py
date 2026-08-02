class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        grid = [[0]*n for _ in range(m)]
        # paths = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j==n-1:
                    continue
                if i == m-1 and j+1 == n-1 or j == n-1 and i+1 == m-1:
                    grid[i][j] = 1
                elif i == m-1:
                    grid[i][j] = grid[i][j+1]
                elif j==n-1:
                    grid[i][j] = grid[i+1][j]
                else:
                    grid[i][j] = grid[i][j+1]+grid[i+1][j]
        return grid[0][0]