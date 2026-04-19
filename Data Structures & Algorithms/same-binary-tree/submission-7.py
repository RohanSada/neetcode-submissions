# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        # BFS 
        from collections import deque
        queue1, queue2 = deque([p]), deque([q])
        while len(queue1) > 0 and len(queue2)>0:
            n1, n2 = len(queue1), len(queue2)
            if n1 != n2:
                return False
            for _ in range(n1):
                node1, node2 = queue1.popleft(), queue2.popleft()
                if node1 is None and node2 is None:
                    continue
                if node1 is None or node2 is None or node1.val != node2.val:
                    return False
                for child in [node1.left, node1.right]:
                    queue1.append(child)
                for child in [node2.left, node2.right]:
                    queue2.append(child)
        return True
        '''

        # DFS

        def traverse(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None or p.val != q.val:
                return False
            left = traverse(p.left, q.left)
            right = traverse(p.right, q.right)
            return left and right
        return traverse(p, q)


            
            
            
            
        