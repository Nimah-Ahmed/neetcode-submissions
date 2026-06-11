# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sameTree(p_node, q_node):
            if p_node == None and q_node == None:
                return True
            elif (p_node == None and q_node != None) or (p_node != None and q_node == None):
                return False
            elif p_node.val != q_node.val:
                return False
            else:
                return sameTree(p_node.left, q_node.left) and sameTree(p_node.right, q_node.right)
        return sameTree(p, q)