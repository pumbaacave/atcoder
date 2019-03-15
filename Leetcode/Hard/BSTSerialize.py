from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = []
        if root is None: return str([])
        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur is None:
                output.append('#')
                continue
            output.append(cur.val)
            queue.extend( [cur.left, cur.right] )
        return str(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return []
        else: data = data[1:-1].split(',')

        def create_node(str_val):
            #if str_val == "'#'":
            if not str_val.isdigit():
                return None
            else:
                return TreeNode(int(str_val))

        root = create_node(data.pop(0))
        queue = deque([root])
        while queue and data:
            node = queue.popleft()
            if not node: continue
            else:
                l_val = data.pop(0)
                r_val = data.pop(0) if data else "#"
                # create child nodes
                l_node = create_node(l_val)
                node.left = l_node
                queue.append(l_node)

                r_node = create_node(r_val)
                node.right = r_node
                queue.append(r_node)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
