import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        heap = []
        c = Counter()
        for num in nums:
            c[num] += 1
        count_num_list = [(count, num) for num, count in c.items()]
        print(count_num_list)
        heapq.heapify(count_num_list)
        res = heapq.nlargest(k,count_num_list)

        return [num for count, num in res]

def test():
    nums =  [1,1,1,2,2,3]
    k = 2
    s = Solution()
    ans = s.topKFrequent(nums, k)

    print(ans)
