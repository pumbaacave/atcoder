from loguru import logger
from collections import defaultdict, deque
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        val_combiations = defaultdict(list)
        queue = deque()
        for num in nums:
            # k: the sum
            # v: list of component that sum up to k
            for k, c_list in val_combiations.items():
                for c in c_list:
                    temp = c[:]
                    temp.append(num)
                    queue.append((k+num, temp))
            for k_com in queue:
                val_combiations[k_com[0]].append(k_com[1])
            queue.clear()
            val_combiations[num].append([num])
        def filter(c_list):
            return {c.sort() for c in c_list if len(c)==3}
                
        return filter(val_combiations[0])


nums = [-1, 0, 1, 2, -1, -4]
# nums = [1, 2, 2, 3]
s = Solution()
answer = s.threeSum(nums)
logger.debug(list(answer))
