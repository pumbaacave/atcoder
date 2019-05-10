class Solution:
  def decodeString(self, s: str) -> str:
    syms = []

    idx, l = 0, len(s)
    def merge(syms):
      base = []
      while syms[-1] != '[':
        base.append(syms.pop())
      else:
        syms.pop()
      b_str = ''.join(reversed(base))
      num = i = 0
      while syms and syms[-1].isnumeric():
        num += int(syms.pop()) * 10 ** i
        i += 1
      syms.append(num * b_str)
    for c in s:
      if c != ']': syms.append(c)
      else: merge(syms)
    return ''.join(syms)

