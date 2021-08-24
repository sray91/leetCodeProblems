# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # an array of integers for result
        result = list()
        # pass in the recursive function 
        self.dfs_recursion(root, result)
        return(result)

    def dfs_recursion(self, node: TreeNode, res: List[int]):
        # the base case 
        if not node: 
            return None

        # recursively traverse the left child node 
        self.dfs_recursion(node.left, res)
        
        # take the value of the vertex node 
        res.append(node.val)
        
        # recursively traverse the right child node 
        self.dfs_recursion(node.right, res)
