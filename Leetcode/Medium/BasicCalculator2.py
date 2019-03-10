class Solution:
    def __init__(self):
        # only have ID_TOKEN and OP_TOKEN
        # ID_TOKEN = "ID"
        order = {
                # op needs action
                # ID_TOKEN: 0,
                "-": 0,
                "+": 0,
                "*": 1,
                "/": 1,
                ")": -1, # all exp can execute before (
                "(": 2, # all exp should wait after following (
                }
        self.order = order

    def calculate(self, s: str) -> int:
        if not s:
            return 0

        tokens = []
        i = 0
        L = len(s)
        # parse phase
        while i < L:
            i, token = self.parse_head(s, i)
            # 0 is valid
            if token is not None:
                tokens.append(token)
        # eval phase
        res = self.eval_tokens(tokens)
        # res = self.clear_paran(res)
        return res

    def clear_paran(self, tokens):
        cleared = []
        while tokens:
            cur = tokens.pop()
            if cur in ('(', ')'):
                continue
            else:
                cleared.insert(0, cur)
        return cleared

    def eval_tokens(self, tokens):
        order = self.order
        stack = []
        while tokens or len(stack) > 1:
            # print(stack, tokens)
            # if not tokens and stack:
            #     # token is empty but len(stack) > 1
            #     # since not () exist
            #     tokens = stack
            #     stack = []
            # else:
            if len(stack) > 1 and stack[-1] not in order and stack[-2] != '(':
                tokens.insert(0, stack.pop())
            else:
                stack.append(tokens.pop(0))


            if not stack:
                continue
            elif stack[-1]  in ("*", "/"):
                op = stack.pop()
                l = stack.pop()
                r = tokens.pop(0)
                res = self.operate(op, l, r)
                tokens.insert(0, res)
            elif stack[-1] in ("+", "-"):
                if self.find_upper_order(stack[-1], tokens):
                    stack.append(tokens.pop(0))
                    stack.append(tokens.pop(0))
                else:
                    op = stack.pop()
                    l = stack.pop()
                    r = tokens.pop(0)
                    tokens.insert(0, self.operate(op, l, r))
            elif stack[-1] == ")":
                stack.pop()
                res = []
                while stack[-1] != "(":
                    res.insert(0, stack.pop())
                stack.pop()
                # tokens in () be processed next
                res = self.eval_tokens(res)
                tokens.insert(0, res)
        # return answer token
        return stack[0]

    def find_upper_order(self, cur, tokens):
        if len(tokens) < 2:
            return False
        elif tokens[0] in self.order:
            return self.order[cur] < self.order[tokens[0]]
        else:
            return self.order[cur] < self.order[tokens[1]]

    def operate(self, op, l, r):
        if op == "+":
            return l + r
        elif op == "-":
            return l - r
        elif op == "*":
            return l * r
        elif op == "/":
            return l // r

    def parse_head(self, s, idx):
        L = len(s)
        if s[idx] == ' ':
            idx += 1
            return idx, None

        elif s[idx].isnumeric():
            j = idx
            while j < L and s[j].isnumeric():
                j += 1
            return j, int(s[idx:j])
        # elif s[idx] in ('(', ')'):
        #     return idx + 1, s[idx]
        else:
            # single char operant
            return idx + 1, s[idx]

def test_find_upper_order():
    s = Solution()
    cur = "+"
    tokens = [1]
    assert s.find_upper_order(cur, tokens) == False
    tokens = [1, "*"]
    assert s.find_upper_order(cur, tokens) == True
    tokens = [1, "+"]
    assert s.find_upper_order(cur, tokens) == False
    tokens = [1, ")"]
    assert s.find_upper_order(cur, tokens) == False

def test_parse():
    s = Solution()
    assert s.parse_head("333", 0) == (3, 333)
    assert s.parse_head(" ", 0) == (1, None)
    assert s.parse_head("+", 0) == (1, "+")
    assert s.parse_head("0", 0) == (1, 0)
    assert s.parse_head("(", 0) == (1, "(")
    assert s.parse_head(")", 0) == (1, ")")

def test_addition():
    s = Solution()
    st = "3 + 2"
    assert s.calculate(st) == eval(st)

def test_eval():
    s = Solution()
    tokens = [3, '+', 2, '*', 5]
    # breakpoint()
    assert s.eval_tokens(tokens) == 13
    tokens = [0]
    assert s.eval_tokens(tokens) == 0

def test_multiply():
    s = Solution()
    st = "3 + 2 * 5"
    assert s.calculate(st) == eval(st)

def test_division():
    s = Solution()
    st = " 3 / 2"
    assert s.calculate(st) == 1
    st = " 3 + 5 / 2"
    assert s.calculate(st) == 5

def test_single_digit():
    s = Solution()
    st = " 0"
    assert s.calculate(st) == 0


def test_paranthesis():
    s = Solution()
    st = " (1 )"
    assert s.calculate(st) == 1
    st = " (2 + 3 )"
    assert s.calculate(st) == eval(st)
    st = " (2 + 3 ) * 3"
    assert s.calculate(st) == eval(st)
    st = "(1+(4+5+2)-3)+(6+8)"
    assert s.calculate(st) == eval(st)

def test_fail_LC():
    st = "(5-(1+(5)))"
    s = Solution()
    assert s.calculate(st) == -1

def test_fail_LC1():
    st = "(7)-(0)+(4)"
    s = Solution()
    assert s.calculate(st) == 11

def test_fail_LC2():
    st = "2-4-(8+2-6+(8+4-(1)+8-10))"
    s = Solution()
    assert s.calculate(st) == -15
