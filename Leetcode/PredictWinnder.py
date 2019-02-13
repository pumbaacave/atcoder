class Solution:
    def PredictTheWinner(self, nums: 'List[int]') -> 'bool':
        first_score = 0
        second_score = 0

        while nums:
            print(nums)
            maximum, nums = self.get_rival_min_gain(nums)
            first_score += maximum
            print(f'first choose {maximum}')
            print(nums)
            maximum, nums = self.get_rival_min_gain(nums)
            second_score += maximum
            print(f'second choose {maximum}')
        return first_score >= second_score

    def get_rival_min_gain(self, nums):
        if not nums:
            return 0, []
        elif len(nums) == 1:
            return nums[0], []
        # select head
        head = nums[0]
        rival_gain_from_tail_nums, head_nums = self.get_max(nums[1:])
        # select tail
        tail = nums[-1]
        rival_gain_from_head_nums, tail_nums = self.get_max(nums[:-1])
        if head - rival_gain_from_tail_nums > tail - rival_gain_from_head_nums:
            return head, nums[1:]
        else:
            return tail, nums[:-1]


        # if rival_gain_from_tail_nums > rival_gain_from_head_nums:
        #     choice = tail
        #     remain_nums = head_nums
        #     return choice, remain_nums
        # elif rival_gain_from_tail_nums < rival_gain_from_head_nums:
        #     choice = head
        #     remain_nums = tail_nums
        #     return choice, remain_nums
        # # case equal
        # elif head > tail:
        #     return head, tail_nums
        # else:
        #     return tail, head_nums


    def get_max(self, nums):
        if not nums:
            return 0, nums
        elif len(nums) == 1:
            return nums[0], []
        else:
            if nums[0] > nums[-1]:
                return nums[0], nums[1:]
            else:
                return nums[-1], nums[:-1]

s = Solution()
Input = [3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1]
ans = s.PredictTheWinner(Input)
print(ans)
