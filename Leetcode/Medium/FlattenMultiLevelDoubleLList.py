"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    @staticmethod
    def link(prv, nxt):
        prv.next = nxt
        nxt.prev = prv

    # return head, tail
    def do_flatten(self, head):
        if not head: return None, None
        # if not head.next: return head, head
        # could have child
        cur = head
        while cur.next:
            nxt = cur.next
            if not cur.child:
                cur = cur.next
                continue
            # flat child
            chd_h, chd_t = self.do_flatten(cur.child)

            self.link(cur, chd_h)
            self.link(chd_t, nxt)
            cur.child = None
            cur = nxt

        if cur.child:
            chd_h, chd_t = self.do_flatten(cur.child)
            self.link(cur, chd_h)
            cur.child = None
            cur = chd_t

        #cur.next = None
        return head, cur

    def flatten(self, head: 'Node') -> 'Node':
        h, t = self.do_flatten(head)
        return h

        