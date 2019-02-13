class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        def gen():
            res = 0
            while True:
                yield res
                res += 1

        def get_or_create_val(key):
            if key in vals:
                return vals[key]
            else:
                val = gen()
                vals[key] = val
                return val

        def get_or_create_equal_val(key, val):
            if key in vals:
                return vals[key]
            else:
                vals[key] = val
                return val

        vals = dict()
        for equation in equations:
            left = equation[0]
            right = equation[3]

            val_left = get_or_create_val(left)
            val_right = get_or_create_equal_val(right, val_left) \
                    if equation[1] == "=" else get_or_create_val(right)
            if equation[1] == "!":
                if val_left == val_right:
                    return False

            elif equation[1] == "=":
                if val_left != val_right:
                    return False
            # else case continue
        # all equation pass
        return True

def test():
    s = Solution()
    equations =["a==b","b==c","a==c"]
    ans = s.equationsPossible(equations)
    assert ans == True
