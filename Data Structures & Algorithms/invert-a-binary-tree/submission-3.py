class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return root


                


                
                