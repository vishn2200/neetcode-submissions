class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        res = []
        if rows == 1 or cols == 1:
            for i in range(rows):
                for j in range(cols):
                    res.append([i,j])
            return res
        res = [[0,cols-1],[rows-1,0]]
        # sol = []
        def dfs(i,j,visited,s,sol):
            nonlocal res
            # nonlocal sol
            if 0 in s and 1 in s:
                if sol[0] not in res:
                    res.append(sol[0])
                return
            if i == rows-1 or j == cols-1:
                s.add(0)
                
            if i == 0 or j == 0:
                s.add(1)
                
            visited[i][j] = True
            # sol.append([i,j])
            if j+1 < cols and not visited[i][j+1] and heights[i][j+1] <= heights[i][j]:
                dfs(i,j+1,visited[:],s,sol)
            if i+1 < rows and not visited[i+1][j] and heights[i+1][j] <= heights[i][j]:
                dfs(i+1,j,visited[:],s,sol)
            if j-1>=0 and not visited[i][j-1] and heights[i][j-1] <= heights[i][j]:
                dfs(i,j-1,visited[:],s,sol)
            if i-1>=0 and not visited[i-1][j] and heights[i-1][j] <= heights[i][j]:
                dfs(i-1,j,visited[:],s,sol)

            # sol.pop()
            # visited.pop()
            if 0 in s and 1 in s:
                if sol[0] not in res:
                    res.append(sol[0])
                return
            return
            
        for i in range(rows):
            for j in range(cols):
                visited = [[False]*cols for _ in range(rows)]
                s = set()
                sol = [[i,j]]
                dfs(i,j,visited,s,sol)
        return res
        
        