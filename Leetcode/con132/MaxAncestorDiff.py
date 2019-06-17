# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        diff = 0
        def helper(node, ancestors):
            nonlocal diff
            if not node: return
            val = node.val
            print(ancestors, val)
            old = diff
            new = max(abs(a - val) for a in ancestors) if ancestors else 0
            diff = max(new, diff)
            ancestors.append(val)
            helper(node.left, ancestors[:])
            helper(node.right, ancestors[:])
        helper(root, [])
        return diff
