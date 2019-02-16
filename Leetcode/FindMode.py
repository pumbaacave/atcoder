tion for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import Counter
class Solution:
    def __init__(self):
        self.cnt = Counter()

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.traverse(root)
        most_common = self.cnt.most_common()
        mode = most_common[0][1]
        ret = []
        for num, count in self.cnt.most_common():
            if count == mode:
                ret.append(num)
            else:
                break
        return ret


    def traverse(self, node):
        if self is None:
            return
        self.cnt[self.val] += 1
        self.traverse(self.left)
        self.traverse(self.right)
        
