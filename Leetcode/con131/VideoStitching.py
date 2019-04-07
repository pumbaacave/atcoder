from collections import namedtuple
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        if clips[0][0] > 0:
            return -1
        stack = []
        Record = namedtuple("Record", "start end last_covered")
        for c in clips:
            # end game
            if stack and stack[-1].end >= T:
                return len(stack)

            # op logic
            if not stack:
                stack.append( Record(c[0], c[1], 0) )
                continue

            # there is a gap
            if c[0] > stack[-1].end:
                return -1
            elif c[1] <= stack[-1].end:
                # can be merged
                continue
            else:
                if c[0] <= stack[-1].start and stack[-1].end <= c[1]:
                    stack[-1] = Record(c[0], c[1], stack[-1].last_covered)
                elif c[0] <= stack[-1].last_covered:
                    stack.pop()
                    stack.append( Record(c[0], c[1], stack[-1].end) )
                else:
                    stack.append( Record(c[0], c[1], stack[-1].end) )
        if stack[-1].end >= T:
            return len(stack)
        else:
            return -1
