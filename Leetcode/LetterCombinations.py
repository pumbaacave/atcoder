from functools import reduce
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mappings = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"],
                }
        def extend(acc, digit):
            if not acc:
                return mappings[digit]
            new_acc = [''.join([c, pre]) for c in mappings[digit] for pre in acc]
            return new_acc
        result = reduce(extend, reversed(digits), [])
        return result
