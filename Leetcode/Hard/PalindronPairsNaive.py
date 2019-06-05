class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # word: index
        worddict = { w:i for i, w in enumerate(words) }
        def is_palin(word):
            return word == word[::-1]
        ret = []

        book = set()
        for i, w in enumerate(words):
            for j in range(len(words) + 1):
                pre = w[:j]
                su = w[j:]
                if pre[::-1] in worddict and is_palin(su):
                    sec_idx = worddict[pre[::-1]]
                    if i != sec_idx and (i, sec_idx) not in book:
                        ret.append([i, sec_idx])
                        book.add((i, sec_idx))
                if su[::-1] in worddict and is_palin(pre):
                    fir_idx = worddict[su[::-1]]
                    if i != fir_idx and (fir_idx, i) not in book:
                        ret.append([fir_idx, i])
                        book.add((fir_idx, i))
        return ret
