# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # DFS traverse & validation DFS
        if not head or not root:
            return False

        def validate(cur, p):
            if p is None:
                return True
            if cur is None:
                return False
            return cur.val == p.val and (validate(cur.left, p.next) or \
                    validate(cur.right, p.next))

        def dfs(node):
            if node is None:
                return False
            if validate(node, head):
                return True
            else:
                return dfs(node.left) or dfs(node.right)
        return dfs(root)
        return False
