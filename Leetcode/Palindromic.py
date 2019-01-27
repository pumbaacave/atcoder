class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 0:
            return s
        
        target_idx = 0
        t_b, t_f = 0, 0
        p_len = 1
        if length == 1:
            return s
        
        for i in range(length):
            f_len = 1
            b_len = 0
            # find 'aaa','aaaa' patter
            # TODO check idx overflow
            while True:
                if self.overflow(length, i, b_len, f_len):
                    break
                if i+f_len < length and s[i] == s[i+f_len]:
                    f_len += 1
                    if f_len + b_len > p_len:
                        p_len = f_len + b_len
                        target_idx = i
                        t_f = f_len
                        t_b = b_len
                    continue
                else:
                    break

            while True:
                b_len += 1
                f_len += 1
                if self.overflow(length, i, b_len, f_len):
                    break
                if s[i-b_len] == s[i+f_len-1]:
                    if f_len + b_len > p_len:
                        p_len = f_len + b_len
                        target_idx = i
                        t_f = f_len
                        t_b = b_len
                else:
                    break
        if p_len == 1:
            return s[0]        
        else:
            return s[target_idx-t_b:target_idx+t_f]
        

    @staticmethod
    def overflow(length, idx, b_len, f_len):
        if idx - b_len < 0 or idx + f_len > length:
            return True
        else:
            return False


def test_conti():
    s = Solution()
    sample = 'aba'
    p_str = s.longestPalindrome(sample)
    print(p_str)
    assert p_str == 'aba'

test_conti()

def test_sample():
    s = Solution()
    sample = 'babad'
    p_str = s.longestPalindrome(sample)
    print(p_str)
    assert p_str == 'bab'

test_sample()

            