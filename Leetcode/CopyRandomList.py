"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        mappings = {None: None}
        def build_next(node):
            if not node:
                return None
            next_copy = build_next(node.next)
            cur_copy = Node(node.val, next_copy, node.random)
            mappings[id(node)] = cur_copy
            return cur_copy

        copy_next = build_next(head.next)
        copy_head = Node(head.val, copy_next, head.random)
        mappings[id(head)] = copy_head

        op_head = copy_head
        while op_head:
            op_head.random = mappings[id(op_head.random) if op_head.random else None]
            op_head = op_head.next
        return copy_head
        
