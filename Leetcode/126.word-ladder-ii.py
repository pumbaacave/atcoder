#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start

from string import ascii_lowercase
from collections import defaultdict
from typing import Set


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words: Set[str] = set(wordList)
        if endWord not in words:
            return []
        # contains lists of paths(also list) which begin word to this word
        # must memo to improve mem efficiency
        path_to_word = defaultdict(set)
        path_to_word[beginWord]

        # dis = 1
        cur_words = set([beginWord])
        words.discard(beginWord)
        while cur_words:
            new_words = set()
            for w in cur_words:
                # iterate N * (len(word) * 26) will be less than N * N when N > 1000
                for i in range(len(w)):
                    for new_ch in ascii_lowercase:
                        new_w = w[:i] + new_ch + w[i+1:]
                        if new_w in words:
                            new_words.add(new_w)
                            path_to_word[new_w].add(w)
            # remove processed words after since there can be multiple same length path
            words -= new_words
            # dis += 1
            # print(new_words)
            # print(path_to_word)
            if endWord in path_to_word:
                break
            cur_words = new_words
        if not path_to_word[endWord]:
            return []
        # BFS
        cond = True
        ret = [[endWord]]
        # build path in reverse order.
        while cond:
            new_ret = []
            elem = None
            for path in ret:
                for pre in path_to_word[path[-1]]:
                    new_ret.append(path + [pre])
                    elem = pre
            ret = new_ret
            # print(ret)
            cond = not (elem == beginWord)

        return [(reversed(p)) for  p in ret ]
        # def dfs(self, path_to_word, )

# @lc code=end
