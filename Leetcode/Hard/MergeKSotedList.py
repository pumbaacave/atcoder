from typing import *
import heapq
# Defition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __lt__(self, other):
        return False

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node) )
        dummy = head = ListNode(None)
        while heap:
            nxt_val, nxt_node = heapq.heappop(heap)
            head.next = nxt_node
            head = head.next
            can = nxt_node.next
            if can:
                heapq.heappush(heap, (can.val, can) )
        return dummy

