class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx, cnt = 0, len(nums)
        for num in nums:
            if num == val:
                cnt -= 1
            else:
                nums[idx] = num
                idx += 1
        print(nums, cnt)
        return cnt 
