from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def next_node(root):
            if not root:
                return root
            queue = deque()
            queue.append(root)
            while queue:
                # print(queue)
                cur = queue.popleft()
                yield cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            yield None

        countered = set()

        gen = next_node(root)
        cur = next(gen)
        # traverse the tree and build a map
        while cur:
            # print(cur.val, countered)
            if (k - cur.val) in countered:
                return True
            else:
                countered.add(cur.val)
                cur = next(gen)
                # print(cur.val)
        return False



