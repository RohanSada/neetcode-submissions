# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        from collections import deque
        if root is None:
            return None
        queue = deque([root])
        while len(queue)>0:
            node = queue.popleft()
            if min(p.val,q.val) < node.val and node.val < max(p.val, q.val):
                return node
            elif p.val < node.val and q.val < node.val:
                queue.append(node.left)
            elif p.val > node.val and q.val > node.val:
                queue.append(node.right)
            elif p.val == node.val or q.val == node.val:
                return node
        return None

        