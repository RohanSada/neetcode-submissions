# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traversal(p, q):
            if not p and not q:
                return True
            if p and q and p.val != q.val:
                return False
            if p and q:
                isSame_l = traversal(p.left, q.left)
                isSame_r = traversal(p.right, q.right)
                return isSame_l and isSame_r
            else:
                return False
        return traversal(p, q)

        