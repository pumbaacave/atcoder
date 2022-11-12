#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # divide left and right, first element from right becomes root
        # recursively.
        self.nums = nums
        return self.map(0, len(nums) - 1)

    # right is inclusive index
    def map(self, left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        if left == right:
            return TreeNode(self.nums[right], None, None)
        mid = (left + right) // 2
        left_node = self.map(left, mid - 1)
        right_node = self.map(mid + 1, right)
        return TreeNode(self.nums[mid], left_node, right_node)


# @lc code=end
