# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # parent node, string search index, current depth
        L = len(S)
        def helper(idx, depth):
            val_start = idx + depth
            if idx + depth >= L or S[idx:val_start] != "-"*depth or idx < 0:
                return None, idx
            next_idx = S.find('-', val_start)
            cur = TreeNode(int(S[val_start:next_idx])) if next_idx > 0 else TreeNode(int(S[val_start:]))

            cur.left, next_idx = helper(next_idx, depth + 1)
            cur.right, next_idx = helper(next_idx, depth + 1)
            return cur, next_idx
        # build root
        idx = S.find('-')
        if idx > 0:
            root = TreeNode(int(S[:idx]))
        else: return TreeNode(int(S))
        root.left, next_idx =helper(idx, 1)
        root.right, next_idx =helper(next_idx, 1)
        return root

