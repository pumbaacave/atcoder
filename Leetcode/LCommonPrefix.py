class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        
        if not strs:
            return ""

        c = 0
        for chars_at_same_idx in zip(*strs):
            if len(set(chars_at_same_idx)) == 1:
                print(chars_at_same_idx)
                c += 1
            else:
                break

                
        return strs[0][:c]
