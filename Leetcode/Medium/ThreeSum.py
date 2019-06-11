class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        l = len(nums) - 1
        nums.sort()
        seen = set()
        ans = []

        def two_sum(target, left):
            if left > l: return []
            right = l
            lrs = []
            if target < 2 * nums[left] or target > 2 * nums[right]:
                return lrs
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    lrs.append([nums[left], nums[right]])
                    left += 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
            return lrs

        for idx, n in enumerate(nums):
            if n in seen:
                continue
            lrs = two_sum(-n, idx + 1)
            for left, right in lrs:
                ans.append([n, left, right])
            seen.add(n)

        def dedup(ans):
            new_a = []
            chk = set()
            for a, b, c in ans:
                hs = (a,b,c)
                if hs in chk:
                    continue
                new_a.append([a, b, c])
                chk.add(hs)
            return new_a
        return dedup(ans)
