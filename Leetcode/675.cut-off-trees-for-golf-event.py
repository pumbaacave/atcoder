#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # Find all location of trees
        # Calculate distance of all  tree pairs, if any paid non reachable, return -1
        # walk from first to last tree to sum up distance.
        if forest[0][0] <= 0:
            return -1

        # build dis dict
        dis = [[float("INF")for f in row] for row in forest]
        #q = deque([(0, 0)])
        # while q:
        #    cur = q.popleft()
        #    cur_val = forest[cur[0]][cur[1]]
        #    for direction in ([])
        N, M = len(forest), len(forest[0])
        seen = set()
        connected = set()
        for m in N:
            for n in M:
                val = forest[m][n]
                # val == 1 not mean a tree.. need to use BFS to form distance
                if val
                if m + 1 < M:
                    down = forest[m+1][n]
                    if down > 0:
                        connected.add((val, down))


# @lc code=end
