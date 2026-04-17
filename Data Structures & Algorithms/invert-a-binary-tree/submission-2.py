class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # this is a bfs approach. In this appriach we will use a queue to keep track of all the nodes in a particular layer. 
        from collections import deque
        if root is None:
            return None
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                for child in [node.left, node.right]:
                    if child == None:
                        continue
                    queue.append(child)
        return root
                


                
                