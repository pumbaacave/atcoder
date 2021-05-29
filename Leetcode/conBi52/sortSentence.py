

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()  # by space
        words = sorted(words, key=lambda word: word[-1])
        return ' '.join(w[:-1] for w in words)
