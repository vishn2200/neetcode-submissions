# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq = deque()
        dq.append(root)
        ans = []
        while dq:
            n = len(dq)
            
            
            level = []
            
            for _ in range(n):
                # print(level)
                node = dq.popleft()
                if node.left: 
                    dq.append(node.left)
                if node.right: 
                    dq.append(node.right)
                level.append(node.val)
            print(level)
            ans.append(level[-1])
        return ans

        