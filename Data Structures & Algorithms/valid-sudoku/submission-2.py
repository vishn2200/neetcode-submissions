class Solution:

    def isValidRow(self, row, board):
        count = 0
        unique = set(board[row])
        if "." in unique:
            unique.remove(".")
        # print(board)
        for i in range(9):
            if board[row][i] != ".":
                if int(board[row][i]) >0 and int(board[row][i])<=9:
                        count+=1
                else:
                    return False
            else:
                continue
        if len(unique) == count:
            return True
        else:
            return False

    def isValidColumn(self, col, board):
        count = 0
        col_values = [board[i][col] for i in range(9)]
        # print(col_values)
        unique = set(col_values)
        if "." in unique:
            unique.remove(".")
        for i in range(9):
            if col_values[i] != ".":
                if int(col_values[i]) >0 and int(col_values[i])<=9:
                    count+=1
                else:
                    return False
            else:
                continue
        if count == len(unique):
            return True
        else:
            return False

    def isValidBoard(self, board):
        print(board)
        flag = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if int(board[i][j]) >0 and int(board[i][j]) <= 9  and int(board[i][j]) not in flag:
                        flag.add(int(board[i][j]))
                    else:
                        return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            
            if not self.isValidRow(i, board):
                return False
            elif not self.isValidColumn(i, board):
                return False
            else:
                if i == 0 or i == 3 or i == 6:
                    
                    for j in range(0, 9, 3):
                        mini = []
                        mini.append(board[i][j:j+3])
                        mini.append(board[i+1][j:j+3])
                        mini.append(board[i+2][j:j+3])
                        if not self.isValidBoard(mini):
                            return False
        return True
