from collections import deque
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.L = max([len(w) for w in words])
        self.buffer = deque()

    def query(self, letter: str) -> bool:
        self.buffer.append(letter)
        if len(self.buffer) > self.L:
            self.buffer.popleft()
        cur = deque()
        for s in reversed(self.buffer):
            cur.appendleft(s)
            if "".join(cur) in self.words:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
