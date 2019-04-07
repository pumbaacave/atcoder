from collections import namedtuple
import heapq
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0

        Coor = namedtuple("Coor", ['v', 'pos'])
        Coor.__lt__ = lambda self, other: self.v < other.v
        M, N = len(matrix), len(matrix[0])
        queue = []
        for i in range(M):
            for j in range(N):
                queue.append(Coor(matrix[i][j], (i, j)))
        heapq.heapify(queue)
        path_len_dict = {}
        while queue:
            cur_coor = heapq.heappop(queue)
            # have neighbour
            dis = 0
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nei = (cur_coor.pos[0] + i, cur_coor.pos[1] + j)
                if nei in path_len_dict and path_len_dict[nei] > dis and matrix[cur_coor.pos[0]][cur_coor.pos[1]]> matrix[nei[0]][nei[1]]:
                    dis = path_len_dict[nei]
            if dis > 0:
                path_len_dict[cur_coor.pos] = dis + 1
            # no neighbour
            else:
                path_len_dict[cur_coor.pos] = 1

        dis = 0
        for k, v in path_len_dict.items():
            if v > dis:
                dis = v
        return dis
