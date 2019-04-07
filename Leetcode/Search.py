class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            m_val = nums[m]
            print(l, r)
            print(m, m_val)
            if m_val == target:
                return m
            elif target < m_val:
                # when search right even if target < m_val
                if target < nums[l] and m_val > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif m_val < target:
                # when search left even if target > m_val
                if target > nums[r] and m_val < nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
