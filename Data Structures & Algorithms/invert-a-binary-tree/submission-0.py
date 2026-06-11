# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if node == None:
                return
            else:
                # Swap node.left and node.right
                left = node.left
                right = node.right
                node.left = right
                node.right = left
                invert(node.left)
                invert(node.right)
        invert(root)
        return root
        