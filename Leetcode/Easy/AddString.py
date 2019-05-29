from itertools import zip_longest
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if not l1 and not l2:
            return '0'
        if not l1:
            return l2
        if not l2:
            return l1
        # num1 is shorter
        if l1 > l2:
            num1, num2 = num2, num1
        stack = []
        carry = 0
        for n1, n2 in zip_longest(reversed(num1), reversed(num2), fillvalue=0):
            carry, now = divmod((int(n1) + int(n2) + carry), 10)
            stack.append(now)
        # add remaining carry if is 1
        if carry:
            stack.append(carry)
        return ''.join(list(map(str, reversed(stack))))
