class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = [[False]*cols for _ in range(rows)]
        def dfs(i,j,visited):
            visited[i][j] = True
            if j+1 < cols and not visited[i][j+1] and board[i][j+1] == "O":
                dfs(i,j+1,visited[:])
            if j-1 >=0 and not visited[i][j-1] and board[i][j-1] == "O":
                dfs(i,j-1,visited[:])
            if i+1 < rows and not visited[i+1][j] and board[i+1][j] == "O":
                dfs(i+1,j,visited[:])
            if i-1 >=0 and not visited[i-1][j] and board[i-1][j] == "O":
                dfs(i-1,j,visited[:])
            return
        for j in range(cols):
            if board[0][j] == "O":
                dfs(0,j,visited)
        for i in range(1,rows):
            if board[i][cols-1] == "O":
                dfs(i,cols-1,visited)
        for j in range(cols-2,-1,-1):
            if board[rows-1][j] == "O":
                dfs(rows-1,j,visited)
        for i in range(rows-2,0,-1):
            if board[i][0] == "O":
                dfs(i,0,visited)

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and board[i][j] == "O":
                    board[i][j] = "X"
        
            
