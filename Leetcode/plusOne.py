class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        carry = 1
        for d in reversed(digits):
            carry, new_d =  divmod(d + carry, 10)
            ret.append(new_d)
        if carry > 0:
            ret.append(carry)
        return reversed(ret)