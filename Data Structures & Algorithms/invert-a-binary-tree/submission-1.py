class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        from collections import deque
        queue = deque([root])
        while len(queue)>0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                for child in [node.left, node.right]:
                    if child==None:
                        continue
                    queue.append(child)
        return root

                


                
                