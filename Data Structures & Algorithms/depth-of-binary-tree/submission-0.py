# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        from collections import deque
        queue = deque([root])
        count = 0
        while len(queue)>0:
            n = len(queue)
            count+=1
            for _ in range(n):
                node = queue.popleft()
                for child in [node.left, node.right]:
                    if child == None:
                        continue
                    queue.append(child)
        return count
        