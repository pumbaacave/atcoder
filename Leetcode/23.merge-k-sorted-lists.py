#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional
from math import inf
from sortedcontainers import SortedKeyList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Sorted:
    def __init__(self, data: List[Optional[ListNode]]):
        self.h = SortedKeyList(data, key=lambda d: -d.val if d else -inf)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.h:
            raise StopIteration()

        while (cur:= self.h.pop()):
            if not cur:
                raise StopIteration()

            n = cur.next
            cur.next = None
            if n is not None:
                self.h.add(n)
            return cur

        raise StopIteration()


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(len(lists) < 1):
            return None
        if(len(lists) < 2):
            return lists[0]
        s = Sorted(lists)
        head = None
        last = None
        for node in s:
            if not head:
                head = node
                last = node
                continue
            last.next = node
            # forward
            last = node
        return head


# @lc code=end
