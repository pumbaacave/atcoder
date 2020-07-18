class Solution:
    def numSub(self, s: str) -> int:
        start = l = s.find('1')       
        # window
        t = 0
        mod = 10 ** 9 + 7
        l_sum = 0
        for ch in s:
            if ch == '1':
                l_sum += 1
            else:
                t += l_sum * (l_sum + 1) / 2
                t %= mod 
                l_sum = 0
        t += l_sum * (l_sum + 1) // 2
        t %= mod
        return int(t)
        
