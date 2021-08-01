class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        num3 = list(map(int, list(num1)))
        num4 = list(map(int, list(num2)))
        ret = [0] * (len(num3) + len(num4) + 1)
        for i, a in enumerate(reversed(num3)):
            carry = 0
            for j, b in enumerate(reversed(num4)):
                d, m = divmod(a * b, 10)
                d1, m1 = divmod(ret[i + j] + m + carry, 10)
                ret[i + j] = m1
                carry = d + d1
            if carry > 0:
                ret[i+j+1] = carry
        ret1 = map(str, reversed(ret))
        ret2 = ''.join(ret1).lstrip('0')
        return ret2 if len(ret2) else '0'
