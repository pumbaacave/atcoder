class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ret = []
        for w in words:
            idx = 0
            delta = w.find(w[0], 1)
            if delta == -1:
                delta = len(w)
            while True:
                idx = text.find(w, idx)
                if idx < 0:
                    break
                ret.append([idx, idx + len(w) - 1])
                idx += delta
        ret.sort(key=lambda x:(x[0], x[1]))
        return ret
