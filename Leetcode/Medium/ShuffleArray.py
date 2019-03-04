from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.orig = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orig
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.orig[:]
        shuffled = []
        length = len(nums)
        for i in range(1, length):
            swap = randint(0, i)
            nums[i], nums[swap] = nums[swap], nums[i]

        return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
