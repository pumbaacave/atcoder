class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        found = False
        l, r = 0, len(nums) - 1
        while l < r:
            cnt = 0
            mid = (l + r) // 2
            if nums[0] == nums[mid]:
                if nums[0] == target:
                    return True
                elif nums[0] < target:
                    while nums[mid % len(nums)] == nums[0]:
                        cnt += 1
                        if cnt >= len(nums):
                            return False
                        mid += 1
                        if mid >= len(nums):
                            r = (l + r) // 2 - 1
                            mid = 0
                elif nums[0] > target:
                    while nums[mid] == nums[0]:
                        cnt += 1
                        if cnt >= len(nums):
                            return False
                        mid -= 1
                        if mid < 0:
                            l = (l + r) // 2 + 1
                            mid = len(nums) - 1
            print(f"l:{l}, r:{r}")
            print(f"m:{mid}, val:{nums[mid]}")
            if nums[0] <= target and nums[0] < nums[mid]:
                n = nums[mid]
            elif nums[0] > target and nums[0] > nums[mid]:
                n = nums[mid]
            elif nums[0] < target and nums[0] > nums[mid]:
                n = float('inf')
            elif nums[0] > target and nums[0] < nums[mid]:
                n = -float('inf')
            elif nums[0] == target:
                return True

            if target == n:
                found = True
                break
            elif target > n:
                l = mid + 1
            else:
                r = mid - 1
        if l == r:
            return nums[l] == target
        
        return found
