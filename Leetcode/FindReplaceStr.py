from itertools import chain
class Solution:
    def findReplaceString(self, S: 'str', indexes: 'List[int]', sources: 'List[str]', targets: 'List[str]') -> 'str':
        if not indexes:
            return S
        # suppose sources are sorted
        res = []
        sorted_params = sorted(zip(indexes, sources, targets), key=lambda x:x[0])
        source_target = chain(sorted_params, [None])
        working_pair = next(source_target)
        i = 0

        while i < len(S):
            if working_pair is not None and i == working_pair[0]:
                # compare and append and forward to next source_target pair
                idx, src, target = working_pair
                # init Flag before comparison
                src_len = len(src)
                if S[i:i+src_len] == src:
                    res.append(target)
                    i += len(src)
                else:
                    res.append(S[i])
                    i += 1

                working_pair = next(source_target)
                pass
            else:
                # append char in original S
                res.append(S[i])
                i += 1
        return "".join(res)

params = (
    "abcd",
    [0, 2],
    ["a", "cd"],
    ["eee", "ffff"],
        )
s = Solution()
ans = s.findReplaceString(*params)
print(ans)
