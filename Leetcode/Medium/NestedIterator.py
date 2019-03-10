# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]


    def next(self):
        """
        :rtype: int
        """
        # if top_list exhausted, iter to new operatable list
        self.hasNext()
        # get next Integer and incr parent idx
        top_list, idx = self.stack[-1]
        num = top_list[idx]
        # incr operaing index of top_list
        self.stack[-1][1] += 1
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        # find next Integer and push it to the top of stack
        s = self.stack
        while s:
            top_list, idx = s[-1]
            # cur op_list is exhausted
            if idx == len(top_list):
                stack.pop()
            else:
                cur = top_list[idx]
                if cur.isInteger():
                    return True
                else:
                    s[-1][1] += 1
                    s.append([cur.getList(), 0])
        return False

class NestedIterator(object):

    def flatten(self, nested):
        # empty list
        if not nested:
            return []
        if isinstance(nested, int):
            return [nested]
        else:
            res = []
            for elem in nested:
                res.extend( self.flatten(elem) )
            return res

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flat = self.flatten(nestedList)
        self.idx = 0
        self.L = len(self.flat)

    def next(self):
        """
        :rtype: int
        """
        num = self.flat[self.idx]
        self.idx += 1
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < self.L
import pytest

@pytest.mark.parametrize("n, expected",[
    ([], []),
    ([1, 2, 3], [1, 2, 3]),
    ([[1, 1], 2, [1, 1]], [1, 1, 2, 1, 1]),
    ([1, [4, [6]]], [1, 4, 6])
    ])
def test_flatten(n, expected):
    pass

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
