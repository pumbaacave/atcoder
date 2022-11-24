#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        self.path_to_me(root, p, path1)
        self.path_to_me(root, q, path2)
        ret = root
        for l, r in zip(path1, path2):
            if l == r:
                ret = l
            else:
                break
        return ret

    def path_to_me(self, parent, me, path: List['TreeNode']):
        if not parent or not me:
            # should not happen
            return
        path.append(parent)
        if parent.val == me.val:
            return
        elif parent.val > me.val:
            return self.path_to_me(parent.left, me, path)
        else:
            return self.path_to_me(parent.right, me, path)
# @lc code=end
