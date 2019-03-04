class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lower = - float('inf')
        padded = [lower] + nums + [lower]
        l, r = 0, len(padded) - 1
        mid = (l + r) // 2

        def is_peak(idx):
            return padded[idx - 1] <  padded[idx] and padded[idx] > padded[idx + 1]

        while True:
            if padded[mid - 1] > padded[mid]:
                r = mid
            elif padded[mid + 1] > padded[mid]:
                l = mid
            else:
                return mid - 1

            mid = (l + r) // 2
