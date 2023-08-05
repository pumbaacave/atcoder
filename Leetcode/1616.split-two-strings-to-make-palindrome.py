#
# @lc app=leetcode id=1616 lang=python3
#
# [1616] Split Two Strings to Make Palindrome
#

# @lc code=start
 def checkPalindromeFormation(self, a, b):
    i, j = 0, len(a) - 1
    while i < j and a[i] == b[j]:
        i, j = i + 1, j - 1
    s1, s2 = a[i:j + 1], b[i:j + 1]

    i, j = 0, len(a) - 1
    while i < j and b[i] == a[j]:
        i, j = i + 1, j - 1
    s3, s4 = a[i:j + 1], b[i:j + 1]
    return any(s == s[::-1] for s in (s1, s2, s3, s4))

# @lc code=end
