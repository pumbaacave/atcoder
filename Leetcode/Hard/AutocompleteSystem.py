from collections import defaultdict
class AutocompleteSystem:

    def input_word(self):
        return ''.join(self.sb)

    def __init__(self, sentences: List[str], times: List[int]):
        self.cnt = defaultdict(int)
        self.sb = []
        self.temp_cnt = None
        for word, fre in zip(sentences, times):
            self.cnt[word] = fre

    def input(self, c: str) -> List[str]:
        # end input
        if c == "#":
            cur_input = self.input_word()
            # save as history
            if cur_input:
                self.cnt[cur_input] += 1
            self.sb.clear()
            self.temp_cnt = None
            return []

        # normal flow
        self.sb.append(c)
        cur_input = self.input_word()
        bucket = []
        for k,v in self.cnt.items():
             if k.startswith(cur_input):
                bucket.append((-v, k))
        return [a for b,a in sorted(bucket)[:3][1]]

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)