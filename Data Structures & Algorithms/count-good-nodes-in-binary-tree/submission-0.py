# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, maxVal):
            if not node:
                return 0
            if node.val >= maxVal:
                count = 1
            else:
                count = 0
            count += traverse(node.left, max(node.val, maxVal))
            count += traverse(node.right, max(node.val, maxVal))
            return count
        
        return traverse(root, root.val)



            
            
        