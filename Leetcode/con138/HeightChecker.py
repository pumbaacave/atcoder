class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if not heights: return 0
        s = sorted(heights)
        return sum(map(lambda x: 1 if x[0] != x[1] else 0, zip(heights, s)))
