from collections import Counter
class Solution:
    def findLHS(self, nums) -> int:
        max_num = - 1 << 12
        max_len = 0
        l, r = 0, 0
        c = Counter(nums)
        max_len = 0
        for k in c.keys():
            if c[k] and c[k + 1]:
                max_len = max(max_len, c[k] + c[k+1])
        return max_len

def test_LHS():
    s = Solution()
    nums = [1,3,2,2,5,2,3,7]
    assert s.findLHS(nums) == 5

