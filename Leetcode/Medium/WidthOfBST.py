
class Solution:
  def widthOfBinaryTree(self, root: TreeNode) -> int:
    if not root: return 0

    # level: leftmost idx, rightmost idx
    large = 2 ** 33
    l_w = {i: large for i in range(33)}
    w = 1
    def helper(node, level, idx):
      if not node: return
      
      w = max(w, idx - l_w[level] + 1)
      if idx < l_w[level][0]:
        l_w[level] = idx

      helper(node.left, level + 1, idx * 2)
      helper(node.right, level + 1, idx * 2 + 1)

    helper(root, 0, 0)

    return w
