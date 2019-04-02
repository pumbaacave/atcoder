# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# in nlogn time

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast = slow = p = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next

            p = slow
            slow = slow.next

        p.next = None
        l = self.sortList(head)
        r = self.sortList(slow)
        # merge
        head = None
        if not l:
            return r
        if not r:
            return l
        while l and r:
            if l.val < r.val:
                if not head:
                    p = head = l
                else:
                    head.next = l
                    head = head.next
                l = l.next
            else:
                if not head:
                    p = head = r
                else:
                    head.next = r
                    head = head.next
                r = r.next
        if l:
            head.next = l
        elif r:
            head.next = r
        return p
