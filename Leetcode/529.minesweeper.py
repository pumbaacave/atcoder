#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
from collections import deque


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        M, N = len(board), len(board[0])
        # BFS
        deq = deque([tuple(click)])
        seen = set()
        while deq:
            pair = deq.popleft()
            if pair in seen:
                continue
            seen.add(pair)
            r, c = pair
            char = board[r][c]
            # already processed or nothng to update
            if char in ('B', 'X', 'M'):
                continue
            if '1' <= char <= '9':
                continue
            # 'E' case
            num_mine = 0
            neighbours = []
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if i == 0 and j == 0:
                        continue
                    r1 = r + i
                    c1 = c + j
                    if r1 < 0 or r1 >= M or c1 < 0 or c1 >= N:
                        continue
                    if board[r1][c1] == 'M':
                        num_mine += 1
                    neighbours.append((r1, c1))
            board[r][c] = str(num_mine) if num_mine > 0 else 'B'
            # propagate at blank
            if num_mine == 0:
                for pair in neighbours:
                    deq.append(pair)

        return board


# @lc code=end
