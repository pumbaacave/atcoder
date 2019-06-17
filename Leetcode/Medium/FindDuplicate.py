class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if fast == slow:
                break
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]
        return slow
def test():
    s = Solution()
    nums = [3,1,3,4,2]
    assert s.findDuplicate(nums) == 3
