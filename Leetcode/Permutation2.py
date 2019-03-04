class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        # all numbers shold be chosen only once, in sequence
        state = []
        total_com = []
        total_per = []

        # push new cur_state to next level
        def bt(cur_state, candidates):
            total_com.append(cur_state)
            if not candidates:
                total_per.append(cur_state)
            
            for i in range(len(candidates)):
                # if i > 0 and candidates[i-1] == candidates[i]:
                #     continue
                # bt(cur_state+[candidates[i]], candidates[:i]+candidates[i+1:])
                # combinatin
                bt(cur_state+[candidates[i]], candidates[i+1:])
        nums.sort()
        bt([], nums)
        print(total_per)
        print(total_com)
        return total_per

        

def test_num_permu():
    s = Solution()
    nums = [1, 1, 2]
    ans = s.permuteUnique(nums)
    assert len(ans) == 3

