class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        def compare_insert(i, pmt):
            temp = pmt[:]
            temp.insert(i, head)
            total_pmt.append(temp)

        if not nums or len(nums) == 1:
            return [nums]

        head = nums[0]
        tails = nums[1:]
        total_pmt = []
        for pmt in self.permuteUnique(tails):
            for i in range(len(pmt)):
                if  head == pmt[i]:
                    continue
                else:
                    compare_insert(i, pmt)
            compare_insert(len(pmt), pmt)
            print(total_pmt)
        return total_pmt

def test_num_permu():
    s = Solution()
    nums = [1, 1, 2]
    ans = s.permuteUnique(nums)
    assert len(ans) == 3

