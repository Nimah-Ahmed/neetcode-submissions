# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, low, high):
            if low < node.val < high:
                if node.left != None and node.right != None:
                    return isValid(node.left, low, min(high, node.val)) and isValid(node.right, max(low, node.val), high)
                if node.left == None and node.right != None:
                    return isValid(node.right, max(low, node.val), high)
                if node.left != None and node.right == None:
                    return isValid(node.left, low, min(high, node.val))
                if node.left == None and node.right == None:
                    return True
            else:
                return False
        return isValid(root, -float('inf'), float('inf'))
