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
        answer_node = ListNode(0)
        l1_nxt = l1.next
        l2_nxt = l2.next
        carry, present_v = divmod(l1.val + l2.val, 10)
        answer_node.val = present_v
        start_node = answer_node
        # both next node are None
        while True:
            if l1_nxt and l2_nxt:
                l1 = l1_nxt
                l2 = l2_nxt
                carry, present_v = divmod(l1.val + l2.val + carry, 10)
                answer_node = self.add_new_node(answer_node, present_v)
                l1_nxt = l1.next
                l2_nxt = l2.next

            elif not l1_nxt and not l2_nxt:
                if carry == 1:
                    new_anser_node = ListNode(carry)
                    answer_node.next = new_anser_node
                # finally return start_node
                return start_node
            else:
                nxt_node = l1_nxt if l1_nxt is not None else l2_nxt
                carry, present_v = divmod(nxt_node.val + carry, 10)
                answer_node = self.add_new_node(answer_node, present_v)
                while True:
                    if nxt_node.next is None:
                        break
                    else:
                        nxt_node = nxt_node.next
                        carry, present_v = divmod(nxt_node.val + carry, 10)
                        answer_node = self.add_new_node(answer_node, present_v)

                if carry == 1:
                    answer_node = self.add_new_node(answer_node, carry)
                return start_node

                


    def add_new_node(self, current_node, nxt_node_val):
            nxt_node = ListNode(nxt_node_val)
            current_node.next = nxt_node
            return nxt_node
        