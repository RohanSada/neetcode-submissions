# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        # BFS
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
        '''

        # DFS

        res = []

        def traverse(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append([])
            res[depth].append(node.val)
            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
        traverse(root, 0)
        return res

            









            




        