
class Solution:
    class Entry():
        def __init__(self, string):
            num_layer = 0
            last = idx = 0
            while string.find('\t', idx) >= 0:
                idx += 1
                num_layer += 1
            self.num_layer = num_layer
            self.name = string[idx:]

        def __repr__(self):
            return f"num_layer: {self.num_layer} \n name: {repr(self.name)}\n"

    def lengthLongestPath(self, input: str) -> int:
        entries = input.split("\n")
        entries = [Solution.Entry(e) for e in entries]
        print(entries)

        cur = 0
        longest_entry = ""

        def update(stack):
            if stack[-1].name.find('.') < 0:
                return

            L = sum([len(e.name) for e in stack])
            L += stack[-1].num_layer
            nonlocal cur, longest_entry
            if L > cur:
                cur = L
                longest_entry = '/'.join([e.name for e in stack ])
        stack = []
        for e in entries:
            if not stack:
                stack.append(e)
                update(stack)
            elif e.num_layer <= stack[-1].num_layer:
                while stack and e.num_layer <= stack[-1].num_layer:
                    stack.pop()
                stack.append(e)
                update(stack)
            else:
                stack.append(e)
                update(stack)
        # print(cur, repr(longest_entry))
        return cur

def test_lpath():
    s = Solution()
    # dir_str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    dir_str = 'a'
    s.lengthLongestPath(dir_str)
