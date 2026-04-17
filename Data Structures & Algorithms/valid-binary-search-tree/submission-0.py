# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            left = traverse(node.left, left, node.val) 
            right = traverse(node.right, node.val, right)
            return left and right
        
        return traverse(root, float("-inf"), float("inf"))            
            
            