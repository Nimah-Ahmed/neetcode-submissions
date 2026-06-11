# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        nested_list = [[root]]
        while nested_list[-1] != []:
            prev_level_set = nested_list[-1]
            new_level_set = []
            for node in prev_level_set:
                if node.left != None:
                    new_level_set.append(node.left)
                if node.right != None:
                    new_level_set.append(node.right)
            nested_list.append(new_level_set)
        
        # Convert to values
        for level_set in nested_list:
            for i, node in enumerate(level_set):
                level_set[i] = node.val
        nested_list.pop(-1)
        return nested_list






