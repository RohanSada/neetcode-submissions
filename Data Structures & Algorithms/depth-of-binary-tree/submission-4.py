# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # BFS Approach:
        if not root:
            return 0
        from collections import deque
        queue = deque([root])
        depth = 0
        while len(queue)>0:
            n = len(queue)
            depth+=1
            for _ in range(n):
                node = queue.popleft()
                for child in [node.left, node.right]:
                    if child is None:
                        continue
                    queue.append(child)
        return depth