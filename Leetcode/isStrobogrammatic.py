class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        l, r = 0, len(num) - 1
        pair = {'1':'1', '6':'9', '9':'6', '8':'8', '0':'0'}
        while l <= r:
            if num[l] in pair and pair[num[l]] == num[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
