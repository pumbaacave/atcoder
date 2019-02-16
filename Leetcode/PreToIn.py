ion for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from collections import deque
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        length = len(preorder)
        if length <= 1:
            return preorder

        queue = deque(preorder)
        process_queue = deque()

        root = TreeNode(queue.popleft())
        process_queue.append(root)
        while True:
            if len(queue) == 0 or len(process_queue) == 0:
                break
            cur = process_queue.pop()
            print(cur.val)
            val = queue.popleft()
            idx = inorder.index(val)
            # boundary check
            if idx+1 < length and inorder[idx+1] == cur.val:
                node = TreeNode(val)
                cur.left = node
                process_queue.append(node)
            elif idx-1 >= 0 and inorder[idx-1] == cur.val:
                node = TreeNode(val)
                cur.right = node
                process_queue.append(node)
            else:
                queue.appendleft(val)

        # inorder traverse
        return root


            #

