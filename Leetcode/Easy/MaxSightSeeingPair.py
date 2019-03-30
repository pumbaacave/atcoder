class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        def update_will_gain(l, new_l):
            return new_l - l - A[l] + A[new_l] > 0
        L = len(A)
        # traverse all possible left

        max_score = 0
        l, val = 0, A[0]
        for i, score in enumerate(A[:-1]):
            if i == l:
                # i = 0
                continue
            max_score = max(max_score, val + score + l - i)
            if update_will_gain(l, i):
                # max_score = 0
                l, val = i, score
            print(l, val)
            print(i, score)

        # TODO op on A[-1]
        max_score = max(max_score, val + A[-1] + l - (L - 1))
        return max_score
