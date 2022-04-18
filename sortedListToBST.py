# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        #recursive function
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        slow, fast = head, head.next
        while (fast.next != None) and (fast.next.next != None):
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        #inserting a null before the mid so the left tree doesn't go through the entire list
        slow.next = None
        root = TreeNode(mid.val)
        #recursion calls
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
        
