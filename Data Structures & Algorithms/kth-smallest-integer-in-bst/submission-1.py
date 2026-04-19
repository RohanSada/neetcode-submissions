# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # 1. Write for the base case 
        # Decide if its gonna be preorder, post order or in order 
        # Take actions based on this by going left, then right

        # Go to the lowest value first 
        # once in the lowest value, start the index from 1 and check if its the required index
        # if yes, return node, else, continue 

        self.count = 0
        self.k_node = None

        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            self.count+=1
            if self.count == k:
                self.k_node = node
            traverse(node.right)

        traverse(root)
        return self.k_node.val
            
            

            
            
            
            



        