from collections import deque
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if not S:
            return ""
        S = S.upper()
        # print(S)
        s_no_dash = ''.join(S.split('-'))
        # print(s_no_dash)

        i = L = len(s_no_dash)
        k_segmented = deque()
        while i >= K:
            k_segmented.appendleft(s_no_dash[i - K: i])
            i = i - K
        if i > 0:
            k_segmented.appendleft(s_no_dash[:i])
        # print(k_segmented)
        # print(k_segmented[0])
        return '-'.join(list(k_segmented))

def test_licence():
    s = Solution()
    S = "5F3Z-2e-9-w"
    K = 4
    assert s.licenseKeyFormatting(S, K) == "5F3Z-2E9W"

