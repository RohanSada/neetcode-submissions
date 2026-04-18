# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        queue = deque([root])

        if not root:
            return []

        BTList = []

        while len(queue)>0:
            n = len(queue)
            layer_list = []
            for _ in range(n):
                node = queue.popleft()
                layer_list.append(node.val)
                for child in [node.left, node.right]:
                    if child is None:
                        continue
                    queue.append(child)
            BTList.append(layer_list)
        return BTList
            




        