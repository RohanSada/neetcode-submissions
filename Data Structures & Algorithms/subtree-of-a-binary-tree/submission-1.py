# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None or q.val != p.val:
                return False
            left = isSame(p.left, q.left)
            right = isSame(p.right, q.right)
            return left and right
        
        def traverse(node, subnode):
            if node is None:
                return False
            same = isSame(node, subnode)
            if same:
                return True
            else:
                left = traverse(node.left, subnode)
                right = traverse(node.right, subnode)
                return left or right
        return traverse(root, subRoot)



            
            
        