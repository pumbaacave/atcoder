#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root, 0)
        return root

    ''' return total sum of current tree
    '''
    def dfs(self, node: TreeNode, sum_lt_me: int) -> int:
        if node is None:
            return 0
        # all right subtree processed
        # pass in sum of nums less than right nodes
        sub_right_sum = self.dfs(node.right, sum_lt_me)
        sum_lt_left = node.val + sub_right_sum + sum_lt_me
        # pass in sum of nums less than left nodes(incl current nodes)
        left_sum = self.dfs(node.left, sum_lt_left)
        old_val = node.val
        node.val = sum_lt_left
        return left_sum + sub_right_sum + old_val


# @lc code=end
