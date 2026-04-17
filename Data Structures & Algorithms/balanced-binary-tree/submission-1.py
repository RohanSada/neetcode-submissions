# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def traversal(node):
            if not node:
                return [True, 0]
            left = traversal(node.left)
            right = traversal(node.right)
            if abs(left[1]-right[1]) > 1:
                bal = False
            else:
                bal = True
            bal_f = (left[0] and right[0]) and bal
            return [bal_f, 1 + max(left[1], right[1])]
        return traversal(root)[0]


            
            
            
