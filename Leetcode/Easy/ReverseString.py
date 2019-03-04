class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) < 2:
            return None
        def helper(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                helper(l + 1, r - 1)

        l, r = 0, len(s) - 1
        helper(l, r)
        
