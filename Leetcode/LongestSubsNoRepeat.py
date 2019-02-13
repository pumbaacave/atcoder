from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        if not s or len(s) == 1:
            return len(s)
        longest_count = 0
        current_count = 0
        i, j = 0, 0
        length = len(s)
        gaurd = set()
        # not touching the right side of s
        while i < length and j < length:
            if s[j] not in gaurd:
                gaurd.add(s[j])
                j += 1
            else:
                longest_count = max(longest_count, j - i)
                gaurd.discard(s[i])
                i += 1
        longest_count = max(longest_count, j - i)

        return longest_count
