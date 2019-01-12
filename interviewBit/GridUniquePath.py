"""
https://www.interviewbit.com/problems/grid-unique-paths/
dynamic programming
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer


    def init_dis(self, h, w):
        dis = []
        for i in range(h):
            dis.append([])
            for _ in range(w):
                dis[i].append(0)
        self.dis = dis

    def uniquePaths(self, A, B):
        self.init_dis(A,B)
        for i in range(A):
            for j in range(B):
                if i == 0 and j == 0:
                    self.dis[i][j] = 1
                elif i == 0:
                    self.dis[i][j] = self.dis[i][j-1]
                elif j == 0:
                    self.dis[i][j] = self.dis[i-1][j]
                else:
                    self.dis[i][j] = self.dis[i-1][j] + self.dis[i][j-1]

        return self.dis[A-1][B-1]

