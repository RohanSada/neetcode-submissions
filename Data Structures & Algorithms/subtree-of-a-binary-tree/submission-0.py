# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse(p, q):
            # if both are None: CONTINUE
            if p == None and q == None:
                return True
            # if one is None and the other is not None
            if p and q and p.val == q.val:
                return traverse(p.left, q.left) and traverse(p.right, q.right)
            else:
                return False
            
        if root is None:
            return False
        from collections import deque
        queue = deque([root])

        while len(queue)>0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                check = traverse(node, subRoot)
                if check == True:
                    return True
                for child in [node.left, node.right]:
                    if child is None:
                        continue
                    queue.append(child)
        return False




        