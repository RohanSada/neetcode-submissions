# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def traverse(node, maxValue):
            nonlocal count
            if not node:
                return 
            if node.val >= maxValue:
                count += 1
                maxValue = node.val
            traverse(node.left, maxValue)
            traverse(node.right, maxValue)
        traverse(root, float("-inf"))
        return count

            
            





            
            
        