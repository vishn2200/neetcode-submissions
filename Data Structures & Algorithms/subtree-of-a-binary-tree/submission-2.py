# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
                    
        def bfs(node):
            de = deque()
            de.append(node)
            l = []
            while de:
                if de[0].left:
                    de.append(de[0].left)
                if de[0].right:
                    de.append(de[0].right)
                l.append(de.popleft().val)
            return l
        if bfs(root) == bfs(subRoot):
            return True
        l_sub = bfs(subRoot)
        dq = deque()
        dq.append(root)
        while dq:
            if dq[0].left and dq[0].left.val == subRoot.val:
                l2 = bfs(dq[0].left)
                if l2 == l_sub:
                    return True
                else:
                    dq.append(dq[0].left)
            elif dq[0].left:
                dq.append(dq[0].left)
            if dq[0].right and dq[0].right.val == subRoot.val:
                l2 = bfs(dq[0].right)
                if l2 == l_sub:
                    return True
                else:
                    dq.append(dq[0].right)
            elif dq[0].right:
                dq.append(dq[0].right)
            dq.popleft()
        return False
            
         