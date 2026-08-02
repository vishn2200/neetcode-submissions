class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            
            last = n
            if target <= matrix[i][n-1]:
                break
        front = 0
        last = n - 1
        mid = (front+last)//2
        while front<=last:
            if target < matrix[i][mid]:
                last = mid-1
                mid = (front+last)//2
            elif target > matrix[i][mid]:
                front = mid + 1
                mid = (front+last)//2
            else:
                return True
        return False

