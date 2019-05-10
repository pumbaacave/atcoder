# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = [], []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        cur_node = None
        carry = 0
        def insert(val, cur_node):
            new_node = ListNode(val)
            new_node.next = cur_node
            cur_node = new_node
            return cur_node
        while num1 and num2:
            carry, cur = divmod(num1.pop() + num2.pop() + carry, 10)
            cur_node = insert(cur, cur_node)
        remain = num1 or num2
        while remain:
            carry, cur = divmod(remain.pop() + carry, 10)
            cur_node = insert(cur, cur_node)
        if carry > 0:
            cur_node = insert(carry, cur_node)
        return cur_node



