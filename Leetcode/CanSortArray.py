class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # find consecutive some bit subgroup
        # find the max if it
        # if local max lower that next subgroup min, ok
        # Otherwise, false
        n0 = nums[0]
        l, h = n0, n0
        # ignore first last_l, force pass first last_h
        last_l, last_h = n0, -1
        # nb = n_bit
        last_nb = self.countSetBits(n0)
            # subgroup: sweeping window
        # 1 
        r = 0
        while r < len(nums):
            # 1
            print(r, nums)
            nums[r]
            while self.countSetBits(nums[r]) == last_nb:
                n = nums[r]
                l = min(l, n)
                h = max(h, n)
                r += 1
                # this end the last group, return final judge
                if r == len(nums):
                    if last_h >= l:
                        return False
                    return True
            else:
                # 1
                last_nb = self.countSetBits(nums[r])
                # 8 > 1
                if last_h >= l:                    
                    return False
                last_l, last_h = l, h
                rr = r + 1
                if rr < len(nums):
                    l, h = nums[rr], nums[rr]
                    r = rr
        # may be start a new subgroup and instantly end, final number is own subgroup
        print(last_h, l)
        if last_h >= l:
            return False
        return True

    def countSetBits(self, n):
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
