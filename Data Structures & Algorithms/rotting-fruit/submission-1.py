class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        # visited = [[False]*n for _ in range(m)]
        de = deque()
        fresh = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    de.append((i,j))
                elif grid[i][j] == 1:
                    fresh.append((i,j))
        print(de)
        while de:
            temp = []
            while de:
                temp.append(de.popleft())
            for y in temp:
                i = y[0]
                j = y[1]
                
                if j+1 < n and grid[i][j+1] == 1 and (i,j+1) not in de:
                    de.append((i,j+1))
                    grid[i][j+1] = 2
                if i+1<m and grid[i+1][j] == 1 and (i+1,j) not in de:
                    de.append((i+1,j))
                    grid[i+1][j] = 2
                if j-1>=0 and grid[i][j-1] == 1 and (i,j-1) not in de:
                    de.append((i,j-1))
                    grid[i][j-1] = 2
                if i-1>=0 and grid[i-1][j] == 1 and (i-1,j) not in de:
                    de.append((i-1,j))
                    grid[i-1][j] = 2
            if len(de) != 0:
                ans+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return ans

        