# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hash table that maps node.val to index in in_order (distinct ?)
        hash_table = {}
        for i, val in enumerate(inorder):
            hash_table[val] = i 
        

        def build(s_pre, e_pre, s_in, e_in):
            # base case
            if s_pre > e_pre and s_in > e_in:
                return None
            if s_pre == e_pre and s_in == e_in:
                return TreeNode(preorder[s_pre], None, None)
            # recursive case
            node = TreeNode(preorder[s_pre])
            index = hash_table[preorder[s_pre]]
            length = index - s_in
            node.left = build(s_pre + 1, s_pre + length, s_in, index - 1)
            node.right = build(s_pre + length + 1, e_pre, index + 1, e_in)
            return node
        return build(0, len(preorder) - 1, 0, len(preorder) - 1)
