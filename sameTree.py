# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            #base case
            if not p and not q:
                return True
            #this will tell you if the structure (nodes) is different or if the structure is the same and values are different
            elif (p and not q) or (q and not p) or (p.val != q.val):
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p,q)