# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        idx = 1
        cur = pre = head
        even_head = even_tail = ListNode(None)
        # create odd and even node list
        while cur:
            if idx % 2 != 0:
                pass
            else:
                pre.next = cur.next
                if pre.next:
                    pre = pre.next
                even_tail.next = cur
                even_tail = even_tail.next

            idx += 1
            cur = cur.next

        even_tail.next = None
        # concatenate even after odd list
        pre.next = even_head.next
        return head
