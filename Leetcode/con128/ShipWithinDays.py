class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        LastU = U = max(weights)
        def cal_num_days(shipload):
            num = 0
            temp = 0
            for w in weights:
                if w <= shipload - temp:
                    temp += w
                else:
                    num += 1
                    temp = w
            return num + 1

        num_days = cal_num_days(U)
        while num_days > D:
            LastU = U
            U *= 2
            num_days = cal_num_days(U)
            # print(U, num_days)
        # print(U, num_days)
        # now num_days <= D
        # binary search
        while LastU < U:
            mid = (LastU + U) // 2
            num_days = cal_num_days(mid)
            # print(mid, num_days)
            if num_days > D:
                LastU = mid + 1
            else:
                U = mid - 1
        return U if cal_num_days(U) <= D else U + 1

