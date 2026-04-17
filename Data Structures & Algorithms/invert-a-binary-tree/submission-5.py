# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        # DFS
        def traverse(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return root
        '''

        # BFS
        if not root:
            return None
        from collections import deque
        queue = deque([root])
        while len(queue)>0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                for child in [node.left, node.right]:
                    if child is None:
                        continue
                    queue.append(child)
        return root





        