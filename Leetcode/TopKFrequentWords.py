from loguru import logger
from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        c = Counter()
        for word in words:
            c[word] += 1

        c_list = [(v, k) for k, v in c.items()]

        level_q = defaultdict(list)
        for word, count in c.items():
            level_q[count].append(word)
        res_list = []
        for key in sorted(level_q.keys(), reverse=True):
            level_q[key].sort()
            length = len(level_q[key])
            if k <= 0:
                break
            if length <= k:
                res_list.extend(level_q[key])
                k -= length
            elif k < length:
                res_list.extend(level_q[key][:k])
                break

        return res_list


def test_topK():
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    s = Solution()
    ans = s.topKFrequent(words, k)
    print(ans)

def test_topK_empty():
    words = []
    k = 2
    s = Solution()
    ans = s.topKFrequent(words, k)
    print(ans)
