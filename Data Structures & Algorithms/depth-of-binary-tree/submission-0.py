# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node == None:
                return 0
            elif node.left == None and node.right == None:
                return 1
            else:
                return 1 + max(depth(node.left), depth(node.right))
        return depth(root)
