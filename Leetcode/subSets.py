class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.do_subsets([], nums)
        return self.ret
    def do_subsets(self, picked, remains):
        # exhausted:
        if not remains:
            self.ret.append(picked)
        else:
            self.do_subsets(picked[:] + [remains[0]], remains[1:])
            self.do_subsets(picked[:], remains[1:])