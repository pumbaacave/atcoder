# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check_bound(cur, lower_limit, upper_limit):
            if cur is None:
                return True

            check_lower = True if lower_limit is None else cur.val > lower_limit
            check_upper = True if upper_limit is None else cur.val < upper_limit

            return check_lower and check_upper


        if root is None:
            return True
        cur = root
        # DFS
        stack = deque()
        # frame: Node, lower_limit, upper_limit
        stack.append((root, None, None))
        while stack:
            cur, lower_limit, upper_limit = stack.pop()
            print(cur)
            print(lower_limit)
            print(upper_limit)
            check_ok = check_bound(cur, lower_limit, upper_limit)
            if not check_ok:
                return False
            # if is a Leaf, continue to next node in stack
            if cur is None:
                continue
            new_upper_limit = min(cur.val, upper_limit) if upper_limit is not None else cur.val
            new_lower_limit = max(cur.val, lower_limit) if lower_limit is not None else cur.val
            # to left child, update upper_limit only
            stack.append((cur.left, lower_limit, new_upper_limit))
            stack.append((cur.right, new_lower_limit, upper_limit))
        return True


