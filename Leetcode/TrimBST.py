# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root: return root
        def is_within(node, L, R):
            if not node:
                return True
            if L <= node.val <= R:
                return True
            return False
        if not is_within(root, L, R):
            if root.val < L:
                return self.trimBST(root.right, L, R)
            else:
                return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        
