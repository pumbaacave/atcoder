class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        M, N = len(workers), len(bikes)
        routes = [[0 for i in range(N)] for j in range(M)]
        for i in range(M):
            for j in range(N):
                routes[i][j] = (abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]))
        print(routes)
        # set wi to bi at first
        total = 0
        owner = dict()
        owns = dict()
        for i in range(M):
            total += routes[i][i]
            owner[i] = i
            owns[i] = i
        for i in range(M):
            using = owns[i]
            gain, new = 0, -1
            for j in range(N):
                if j in owner:
                    b = owner[j]
                    delta = routes[i][using] + routes[b][j] - routes[i][j] - routes[b][using]
                else:
                    delta = routes[i][using] - routes[i][j]

                if delta > gain:
                    gain = delta
                    new = j

            if gain > 0:
                # swap
                if new in owner:
                    b = owner[new]
                    owner[using] = b
                    owns[b] = using
                    owner[new] = i
                    owns[i] = new
                else:
                    del owner[i]
                    owner[new] = i
                    owns[i] = new
                total += gain

        return total
