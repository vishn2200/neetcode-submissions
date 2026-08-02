# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif not q and p:
            return False
        dq = deque()
        dq2 = deque()
        dq.append(p)
        dq2.append(q)
        def bfs(de):
            l = []
            while de:
                if de[0] != 0:
                    if de[0].left:
                        de.append(de[0].left)
                    else:
                        de.append(0)
                    if de[0].right:
                        de.append(de[0].right)
                    else:
                        de.append(0)
                    
                    l.append(de.popleft().val)
                else:
                    l.append(de.popleft())
               
            return l
        l1 = bfs(dq)
        l2 = bfs(dq2)
        if l1 == l2:
            return True
        else:
            return False