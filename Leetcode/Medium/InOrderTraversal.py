# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def doTraverse(self, node):
        if not node:
            return

        self.doTraverse(node.left)
        self.res.append(node.val)
        self.doTraverse(node.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []

        self.doTraverse(root)

        return self.res
