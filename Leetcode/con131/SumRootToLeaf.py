# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        total = 0
        def helper(node, parent_val):
            nonlocal total
            if not node:
                return
            cur_val = parent_val * 2 + node.val
            if not node.left and not node.right:
                total += cur_val
            else:
                helper(node.left, cur_val)
                helper(node.right, cur_val)
        helper(root, 0)
        return total
