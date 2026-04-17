# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''        
        def traverse(root):
            if root is None:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            return 1 + max(left, right)
        return traverse(root)
        '''
        
        from collections import deque
        if root is None:
            return 0
        queue = deque([root])
        max_length = 0
        while len(queue)>0:
            n = len(queue)
            max_length+=1
            for _ in range(n):
                node = queue.popleft()
                for child in [node.left, node.right]:
                    if child is None:
                        continue
                    queue.append(child)
        return max_length
