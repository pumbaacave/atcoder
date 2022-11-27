#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from typing import List
from string import ascii_lowercase
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words: Set[str] = set(wordList)
        if endWord not in words:
            return 0

        dis = 1
        cur_words = [beginWord]
        words.discard(beginWord)
        while cur_words:
            new_words = []
            for w in cur_words:
                if w == endWord:
                    return dis
                # iterate N * (len(word) * 26) will be less than N * N when N > 1000
                for i, ch in enumerate(w):
                    for new_ch in ascii_lowercase:
                        new_w = w[:i] + new_ch + w[i+1:]
                        if new_w in words:
                            new_words.append(new_w)
                            words.discard(new_w)
            dis += 1
            # print(new_words)
            cur_words = new_words

        return 0

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build n * n adacent list
        end_idx = -1
        begin_idx = -1
        begin_nei = set()
        for i, w in enumerate(wordList):
            if w == endWord:
                end_idx = i
            if w == beginWord:
                begin_idx = i
            # if self.is_neighbour(beginWord, w):
            #     begin_nei.add(i)
        if end_idx < 0:
            # not reachable
            return 0
        # beginWord not in workdList
        if begin_idx < 0:
            begin_idx = len(wordList)
            wordList.append(beginWord)
        begin_nei.add(begin_idx)
        # update: no need to do so.
        # calculate all shortest distance between all nodes.
        N = len(wordList)
        # adjacent list
        adj = collections.defaultdict(set)
        for i, w in enumerate(wordList):
            # half the time further...
            for j, q in enumerate(wordList[i+1:], i+1):
                if self.is_neighbour(w, q):
                    adj[i].add(j)
                    adj[j].add(i)
        # +1 means add the begin word
        ret = self.cal_dis(adj, begin_idx, end_idx) + 1
        # 0 if not reachable
        return ret if ret <= N else 0

    def cal_dis(self, adj, start, end):
        # BFS, dikstra
        # even priority queue is too slow for this case
        # 1. cache distance to skip sifting
        # 2. double end BFS to reduce search space/diameter
        q1 = set([start])
        q2 = set([end])
        seen1 = set()
        seen2 = set()
        dis_q1 = 0
        dis_q2 = 0
        while q1 and q2:
            new_q1 = set()
            new_q2 = set()
            for nei in q1:
                if nei in q2:
                    return dis_q1 + dis_q2
                seen1.add(nei)
                for new_n in adj[nei]:
                    if new_n not in seen1:
                        new_q1.add(new_n)
            dis_q1 += 1
            q1 = new_q1
            # q1 forwarded by 1 round
            for nei in q2:
                if nei in q1:
                    return dis_q1 + dis_q2
                seen2.add(nei)
                for new_n in adj[nei]:
                    if new_n not in seen2:
                        new_q2.add(new_n)
            dis_q2 += 1
            q2 = new_q2

        # not reachable
        return float('INF')

    def is_neighbour(self, left, right):
        # all words of the same length
        num_diff = 0
        # for l, r in zip(left, right):
        for i in range(len(left)):
            l = left[i]
            r = right[i]
            if l != r:
                num_diff += 1
            # early return to spedify python :)
            if num_diff > 1:
                return False
        return num_diff == 1

# @lc code=end
