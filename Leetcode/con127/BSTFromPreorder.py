# tion for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        val = preorder[0]
        cur = TreeNode(val)
        left_vals = filter(lambda x:x < val, preorder[1:])
        right_vals = filter(lambda x: x > val, preorder[1:])
        left = self.bstFromPreorder(list(left_vals))
        right = self.bstFromPreorder(list(right_vals))
        cur.left = left
        cur.right = right
        return cur
