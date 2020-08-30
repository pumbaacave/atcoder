# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # index at most from -1000, 1000
        state = collections.defaultdict(list)

        def dfs(node, x_idx, y_idx):
            if not node:
                return
            state[x_idx].append((-y_idx, node.val))
            dfs(node.left, x_idx - 1, y_idx - 1)
            dfs(node.right, x_idx + 1, y_idx - 1)
        dfs(root, 0, 0)

        def mapper(mark):
            mark.sort()
            return list(map(lambda x: x[1], mark))
        return [mapper(state[key]) for key in sorted(state.keys())]
