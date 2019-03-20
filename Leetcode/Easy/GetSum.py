import math
class Solution(object):
    def getSum(self, a, b):
        """
        bit operations
        suppose a, b are int32
        :type a: int
        :type b: int
        :rtype: int
        """
        result = 0
        carry = 0
        carry_on = {(0,0,0), (0,0,1), (1,0,0), (0,1,0)}

        for i in range(32):
            a_lsb = a & 1
            b_lsb = b & 1
            cur = a_lsb ^ b_lsb ^ carry
            carry = 0 if (a_lsb, b_lsb, carry) in carry_on else 1

            result |= cur << i
            a = a >> 1
            b = b >> 1
        # result is negative number
        if result >> 31 & 1 == 1:
            new_result = 0
            for i in range(32):
                result_lsb = result & 1
                new_bit = ~result_lsb & 1
                new_result |= new_bit << i

                result = result >> 1
            result = -(new_result + 1)
        return result

import pytest

@pytest.mark.parametrize("a, b, expected",[
    (3, 2, 5),
    (0, 0, 0),
    (-1, 3, 2),
    (-27, 7, -20)
    ])
def test_bit_sum(a, b, expected):
    s = Solution()
    assert expected == s.getSum(a, b)

