# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import copy
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def cal_len(head):
            print(id(head))
            cnt = 0
            while head:
                cnt += 1
                print(id(head))
                head = head.next
            return cnt
        # ca, cb = copy.copy(headA), copy.copy(headB)
        lenA, lenB = cal_len(headA), cal_len(headB)
        if lenA < lenB:
            # headA is longer
            headA, headB = headB, headA
        delta = abs(lenA - lenB)
        while delta:
            delta -= 1
            headA = headA.next
        while headA and headB and headA.val != headB.val:
            headA = headA.next
            headB = headB.next
        if headA:
            return headA
        else:
            return None

