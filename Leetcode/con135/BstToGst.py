# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # right child first post order DFS
        total = 0
        def dfs(node):
            nonlocal total
            if not node:
                return
            else:
                dfs(node.right)
                total += node.val
                node.val = total
                dfs(node.left)
        dfs(root)
        return root
