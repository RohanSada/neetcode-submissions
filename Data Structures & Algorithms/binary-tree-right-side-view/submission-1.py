# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if root is None:
            return []

        right_most_values = []

        queue = deque([root])
        while len(queue)>0:
            n = len(queue)
            layer_values = []
            for _ in range(n):
                node = queue.popleft()
                layer_values.append(node.val)
                for child in [node.left, node.right]:
                    if child == None:
                        continue
                    queue.append(child)
            right_most_values.append(layer_values[-1])
        return right_most_values





        