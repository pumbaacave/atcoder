class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str_M = ''
        str_hdr = ''
        str_hdr_com = ''
        str_ten = ''
        str_ten_com = ''
        str_last = ''
        str_M, res = self.build_M(num)
        # res should be in [0, 999]
        if res >= 900:
            str_hdr, res = self.build_CM(res)
        elif res >= 500:
            str_hdr, res = self.build_D(res)
        elif res >= 400:
            str_hdr, res = self.build_CD(res)

        str_hdr_com, res = self.build_C(res)
        # res should be in [0, 99]
        if res >= 90:
            str_ten, res = self.build_XC(res)
        elif res >= 50:
            str_ten, res = self.build_L(res)
        elif res >= 40:
            str_ten, res = self.build_XL(res)

        str_ten_com, res = self.build_X(res)
        # res should be in [0, 9]
        if res == 9:
            str_last = 'IX'
        elif res >= 5:
            str_last = ''.join(['V', 'I'*(res-5)])
        elif res == 4:
            str_last = 'IV'
        else:
             str_last = 'I' * res
        
        return ''.join([str_M, str_hdr, str_hdr_com, str_ten, str_ten_com, str_last])


    def build_M(self, num):
        div, mod = divmod(num, 1000)
        str_M = 'M' * div
        return str_M, mod

    def build_CM(self, num):
        div, mod = divmod(num, 900)
        return 'CM', mod

    def build_D(self, num):
        div, mod = divmod(num, 500)
        return 'D', mod

    def build_CD(self, num):
        div, mod = divmod(num, 400)
        return 'CD', mod

    def build_C(self, num):
        div, mod = divmod(num, 100)
        str_C = 'C' * div
        return str_C, mod

    def build_XC(self, num):
        div, mod = divmod(num, 90)
        return 'XC', mod

    def build_L(self, num):
        div, mod = divmod(num, 50)
        return 'L', mod

    def build_XL(self, num):
        div, mod = divmod(num, 40)
        return 'XL', mod

    def build_X(self, num):
        div, mod = divmod(num, 10)
        str_X = 'X' * div
        return str_X, mod
        

def test_sample1():
    num = 1994
    s = Solution()
    answer = s.intToRoman(num)
    assert answer == "MCMXCIV"

def test_M():
    num = 2003
    s = Solution()
    str_M, mod = s.build_M(num)
    assert str_M == 'MM'
    assert mod == 3

def test_C():
    num = 303
    s = Solution()
    str_M, mod = s.build_C(num)
    assert str_M == 'CCC'
    assert mod == 3

def test_CM():
    num = 903
    s = Solution()
    str_M, mod = s.build_CM(num)
    assert str_M == 'CM'
    assert mod == 3

def test_D():
    num = 503
    s = Solution()
    str_M, mod = s.build_D(num)
    assert str_M == 'D'
    assert mod == 3

def test_CD():
    num = 403
    s = Solution()
    str_M, mod = s.build_CD(num)
    assert str_M == 'CD'
    assert mod == 3

def test_X():
    num = 33
    s = Solution()
    str_M, mod = s.build_X(num)
    assert str_M == 'XXX'
    assert mod == 3

def test_XC():
    num = 93
    s = Solution()
    str_M, mod = s.build_XC(num)
    assert str_M == 'XC'
    assert mod == 3

def test_L():
    num = 53
    s = Solution()
    str_M, mod = s.build_L(num)
    assert str_M == 'L'
    assert mod == 3

def test_XL():
    num = 43
    s = Solution()
    str_M, mod = s.build_XL(num)
    assert str_M == 'XL'
    assert mod == 3