# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        flag = -1
        def dfs(root):
            nonlocal flag
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left-right) > 1:
                flag = 1
            return max(1+dfs(root.left),1+dfs(root.right))
        dfs(root)
        if flag == 1:
            return False
        else:
            return True
