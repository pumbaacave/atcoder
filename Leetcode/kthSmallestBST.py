# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # inorder travel
        cnt = 0
        cur = root
        stack: List[TreeNode] = [root]
        # invariance: node can enter stack only after all left children processed
        while cur:
            stack.append(cur)
            cur = cur.left
        while stack:
            cur = stack.pop(-1)
            # process left child 
            # process current 
            cnt += 1
            if cnt == k:
                return cur.val
            cur = cur.right
            # process right child 
            while cur
                stack.append(cur)
                cur = cur.left
        return -1
        
        