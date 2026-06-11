# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        node_to_pathsum = {}
        def pathsum(node):
            if node == None:
                return 0
            if node.left == None and node.right == None:
                node_to_pathsum[node] = node.val
                return node.val
            else:
                left_pathsum = pathsum(node.left)
                right_pathsum = pathsum(node.right)
                print(left_pathsum, right_pathsum, node.val)
                max_pathsum_total =  max(
                    left_pathsum + node.val,
                    right_pathsum + node.val,
                    left_pathsum + right_pathsum + node.val,
                    node.val)
                node_to_pathsum[node] = max_pathsum_total
                max_pathsum = max(
                    left_pathsum + node.val,
                    right_pathsum + node.val,
                    node.val
                )
                return max_pathsum
        root_pathsum = pathsum(root)
        print("---")
        print(node_to_pathsum)
        return max(node_to_pathsum.values())
    