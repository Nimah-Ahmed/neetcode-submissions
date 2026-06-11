# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        hash_table = {}
        def depth(node):
            if node == None:
                if 0 not in hash_table:
                    hash_table[0] = {node}
                else:
                    hash_table[0].add(node)
                return 0
            if node.left == None and node.right == None:
                if 1 not in hash_table:
                    hash_table[1] = {node}
                else:
                    hash_table[1].add(node)
                return 1
            else:
                depth_val = 1 + max(depth(node.left), depth(node.right))
                if depth_val not in hash_table:
                    hash_table[depth_val] = {node}
                else:
                    hash_table[depth_val].add(node)
                return depth_val
        hash_table = {}
        subRoot_depth = depth(subRoot)
        hash_table = {}
        depth(root)

        def sameTree(p_node, q_node):
            if p_node == None and q_node == None:
                return True
            elif p_node != None and q_node == None:
                return False
            elif p_node == None and q_node != None:
                return False
            elif p_node.val != q_node.val:
                return False
            else:
                return sameTree(p_node.left, q_node.left) and sameTree(p_node.right, q_node.right)
        
        if subRoot_depth not in hash_table:
            return False
        else:
            subtrees = hash_table[subRoot_depth]
            for subtree in subtrees:
                is_Same = sameTree(subtree, subRoot)
                if is_Same:
                    return True
            return False
            


        
         
