class Solution:
    def PredictTheWinner(self, nums: 'List[int]') -> 'bool':

        #dp[i][j] result PredictTheWinner of [i,j]
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            # (is_win, my_score, rival_score)
            dp[i][i] = (True, (nums[i], 0))
        # for i in range(length-1):
        #     dp[i][i+1] = (True, (nums[i], 0))

        # TODO: check boundary
        for w in range(1, length):
            # TODO: check bounday
            for i in range(length-w):
                res_when_head = dp[i+1][i+w]
                res_when_tail = dp[i][i+w-1]
                # lose either way
                head_score = res_when_head[1][1] + nums[i]
                tail_score = res_when_tail[1][1] + nums[i+w]
                # TODO: equal sign
                if head_score >= tail_score:
                    my_score = head_score
                    rival_score = res_when_head[1][0]
                else:
                    my_score = tail_score
                    rival_score = res_when_tail[1][0]

                is_win = my_score >= rival_score
                dp[i][i+w] =(is_win, (my_score, rival_score))


        print(dp[0][length-1])
        return dp[0][-1][0]


s = Solution()
input_list = [3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1]
ans = s.PredictTheWinner(input_list)
print(ans)
