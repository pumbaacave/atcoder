from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str])-> str:
        ban_set = set(banned)
        buffer = []
        w_cnt = defaultdict(int)

        def add_to_cnt():
            if len(buffer) <= 0:
                return
            else:
                w_cnt[''.join(buffer).lower()] += 1
                buffer.clear()
        for ch in paragraph:
            if not ch.isalpha():
                add_to_cnt()
            else:
                buffer.append(ch)
        add_to_cnt()

        key = ''
        cnt = 0
        for k, v in w_cnt.items():
            if k not in ban_set and v > cnt:
                cnt = v
                key = k
        return key
