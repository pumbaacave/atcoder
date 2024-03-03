from math import ceil
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        # find the last chunk at see if 1 chuck orver lap
        # if not reconstruct the whole string
        N = len(word)
        div, res = divmod(N, k)
        # find at least 1 chunk
        if(res == 0):
            res = k
        #print(idx)
        overlap = 0
        # how to get lat chunk differs when res == 0
        for i in range(div):
            chunk = word[N - i * k - res:]
            #print(chunk)
            if(len(chunk) == N):
                continue
            if word.find(chunk) == 0:
                overlap =  i + 1
            # it is OK 2 chunk fail to last 3 chunk ok

        #print(overlap)
        ret = 0
        if overlap:
            ret = ceil(N/ k) - overlap
        else:
            ret = ceil(N/ k)
        # at least 1 ops required
        return max(ret, 1)
            
