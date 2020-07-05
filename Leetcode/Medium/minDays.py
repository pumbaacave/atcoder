class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        self.batch = k
        self.len = len(bloomDay)
        self.state = dict()
        self.data = bloomDay
        # state: (idx, num_remain)
        def dp(idx, num):
            if num == 0: return 0
            if (idx, num) in self.state:
                return self.state[(idx, num)]
            if num * self.batch > self.len - idx:
                self.state[(idx, num)] = -1
                return -1
            global_min = float('Inf')
            for i in range(idx, self.len - self.batch + 1):
                remain = dp(i+self.batch, num -1)
                if remain == -1:
                    continue
                sub_min = max(  max(self.data[i:i+self.batch]) , remain)
                global_min = min(global_min, sub_min)
            self.state[(idx,num)] = global_min
            return global_min
        dp(0, m)
        print(self.state)
        return dp(0,m)
