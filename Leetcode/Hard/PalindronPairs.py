from typing import *
from collections import defaultdict
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Trie solution
        node = lambda: defaultdict(node)
        root = node()['']
        for i, w in enumerate(words):
            cur = root
            if w == "":
                root['#'] = i
                continue
            for c in reversed(w):
                cur = cur[c]
            cur['#'] = i # end_flad: word_idx
        answer = []
        def remain_same(c, j, w):
            for x in w[j:]:
                if x != c: return False
            return True
        for i, w in enumerate(words):
            cur = root
            for j, c in enumerate(w):
                cur = cur[c]
                if '#' in cur and i!= cur['#'] and remain_same(c,j, w):
                    answer.append([i, cur['#']])

            if '#' in cur and i!= cur['#'] and remain_same(c,j, w):
                answer.append([i, cur['#']])

            for c in cur.keys():
                if not c.isalpha():
                    continue
                while c in cur:
                    cur = cur[c]
                if "#" in cur and i != cur['#']:
                    answer.append([i, cur['#']])
        return answer

def test_pairs():
    s = Solution()
    words = ["abcd","dcba","lls","s","sssll"]
    print(s.palindromePairs(words))


def test_sp():
    s = Solution()
    words = ["a",""]
    print(s.palindromePairs(words))
