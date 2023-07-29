#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # suppose all interval in a group is sorted, easier to handle the constrains
        # restriction: last's right decides what next is possible
        # big left come first so that it is consumed first(gap smaller)
        # if smal left come first it take longer to find the right group to fit in(python runtime wil TTL)
        # intervals = sorted(intervals, key=lambda x: (x[1]))
        # groups of right
        # groups = []
        # for itv in intervals:
        #    # since intervals are sorted by right, we can insert and keep it sorted
        #    # groups = sorted(groups)
        #    # i can be 0 at first
        #    BIG = 10 ** 7
        #    for i in range(len(groups)-1, -1, -1):
        #        # check last's right against itv's left := intersection
        #        if groups[i] < itv[0]:
        #            # remove this group and append current itv to the end of groups
        #            del groups[i]
        #            # maybe del from list is too slow, use tombstone instead
        #            # groups[i] = BIG
        #            # break groups loop
        #            break

        #    groups.append(itv[1])

        # return len([g for g in groups if g < BIG])
        # return len(groups)

        # いもす法でした
        # sweep line
        A = []
        for a,b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])
        res = cur = 0
        for a, diff in sorted(A):
            cur += diff
            res = max(res, cur)
        return res

# @lc code=end
