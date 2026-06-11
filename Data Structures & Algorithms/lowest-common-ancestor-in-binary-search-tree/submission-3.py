# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Label all nodes that have p or q as children, including p,q
        # Find(p)
        hash_table = {}
        def find(T, k):
            if T is None:
                return None
            if T.val < k.val:
                returned_val = find(T.right, k)
                if returned_val != None:
                    if T not in hash_table:
                        hash_table[T] = {k}
                    else:
                        hash_table[T].add(k)
                return returned_val
            if T.val > k.val:
                returned_val = find(T.left, k)
                if returned_val != None:
                    if T not in hash_table:
                        hash_table[T] = {k}
                    else:
                        hash_table[T].add(k)
                return returned_val
            else:
                if T not in hash_table:
                    hash_table[T] = {k}
                else:
                    hash_table[T].add(k)
                return T
        
        dummy_p = find(root, p)
        dummy_q = find(root, q)

        lca_node = [None]
        def find_LCA(T, k):
            if T is None:
                return None
            if T.val > k.val:
                returned_val = find_LCA(T.left, k)
                if returned_val != None:
                    if hash_table[T] == {p, q} and lca_node == [None]:
                        lca_node[0] = T
                return returned_val
            if T.val < k.val:
                returned_val = find_LCA(T.right, k)
                if returned_val != None:
                    if hash_table[T] == {p, q} and lca_node == [None]:
                        lca_node[0] = T
                return returned_val
            else:
                if T != None:
                    if hash_table[T] == {p, q} and lca_node == [None]:
                        lca_node[0] = T
                return T
        dummy_p = find_LCA(root, p)
        return lca_node[0]
        
        
