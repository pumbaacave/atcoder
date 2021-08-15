from collections import ChainMap, deque
class Solution:
    """
    implement Calculator usins ShuntingYard + Postfix expression
    """
    def __init__(self):
        # only have ID_TOKEN and OP_TOKEN
        # ID_TOKEN = "ID"
        # left associate operation
        left_op = {
                # op needs action
                # ID_TOKEN: 0,
                "-": 0,
                "+": 0,
                "*": 1,
                "/": 1,
                }
        right_op = {
                "^": 2
                }
        # non-associate
        paren = {
                ")": -1, # all exp can execute before (
                "(": 2, # all exp should wait after following (
                }
        self.op = ChainMap(left_op, right_op, paren)
        self.left_op = left_op
        self.right_op = right_op
        self.paren = paren

    def calculate(self, s: str) -> int:
        if not s:
            return 0

        tokens = self.parse_to_tokens(s)
        res = self.eval(tokens)
        return res

    def eval(self, tokens):
        postfix_expression = self.shunting_yard(tokens)
        return self.eval_postfix(postfix_expression)

    def top_is_executed_earlier(self, coming_token, op_stack):
        """
        there is a top token of op_stack and it should be executed earlier
        """
        def is_top_higher_priority(coming_token, top_token):
            return self.op[top_token] > self.op[coming_token]
        def equal_left_on_left(coming_token, top_token):
            # same priority require pop out first
            # exp: coming "+", top is "-", pop out "-" first
            if coming_token in self.left_op and top_token in self.left_op:
                return self.op[coming_token] == self.op[top_token]
        if not op_stack:
            return False
        else:
            top_token = op_stack[-1]
            if coming_token == "(":
                return False
            if top_token == "(":
                return False
            if is_top_higher_priority(coming_token, top_token):
                return True
            elif equal_left_on_left(coming_token, top_token):
                return True
            # now only have one kind of right associate operator
            # if higher_right_on_left(comint_token, top_token):
            #     return True
            return False
    def shunting_yard(self, tokens):
        op_stack = deque()
        exp_stack = deque()
        for token in tokens:
            if not self.is_op(token):
                exp_stack.append(token)
            elif token != ")":
                while self.top_is_executed_earlier(token, op_stack):
                    exp_stack.append( op_stack.pop() )
                else:
                    op_stack.append(token)
            elif token == ")":
                while op_stack[-1] != "(":
                    exp_stack.append( op_stack.pop() )
                else:
                    # drop "(" and ")"
                    op_stack.pop()

        while op_stack:
            # move remain op_token to exp_stack
            exp_stack.append( op_stack.pop() )
        return exp_stack


    def is_op(self, token):
            return token in self.op

    def eval_postfix(self, postfix_expression):
        """
        param postfix_expression:: List[Token] in postfix order
        """
        token_stack = deque()
        for token in postfix_expression:
            if not self.is_op(token):
                token_stack.append(token)
            else:
                operant = token
                rhs = token_stack.pop()
                lhs = token_stack.pop()
                result = self.operate(operant, lhs, rhs)
                token_stack.append(result)
        assert len(token_stack) == 1
        return token_stack.pop()

    def parse_to_tokens(self, s):

        tokens = []
        i = 0
        L = len(s)
        # parse phase
        while i < L:
            i, token = self.parse_head(s, i)
            # 0 is valid
            if token is not None:
                tokens.append(token)
        return tokens

    def operate(self, op, l, r):
        if op == "+":
            return l + r
        elif op == "-":
            return l - r
        elif op == "*":
            return l * r
        elif op == "/":
            return l / r
        elif op == "^":
            return l ** r

    def parse_head(self, s, idx):
        # idx to start parsing
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

import pytest

@pytest.mark.parametrize("coming_token, op_stack, judge",[
    ("+", [], False),
    ("+", ["-"], True),
    ("-", ["+"], True),
    ("*", ["-"], False),
    ("/", ["-"], False),
    ("+", ["("], False),
    ("-", ["("], False),
    ("*", ["("], False),
    ("/", ["("], False),
    ("(", ["/"], False),
    ])
def test_top_is_executed_earlier(coming_token, op_stack, judge):
    s = Solution()
    assert s.top_is_executed_earlier(coming_token, op_stack) == judge

@pytest.mark.parametrize("tokens, postfix_expression",[
    ([0], [0]),
    ([3, "+", 2], [3, 2, "+"]),
    ([3, "+", 4, "*", 2], [3, 4, 2, "*", "+"]),
    (["(", 0, ")"], [0]),
    ([4, "*", "(", 2, "+", 3, ")"], [4, 2, 3, "+", "*"]),
    ([4, "*", 2, "+", 3], [4, 2, "*", 3, "+"]),
    ([3, "+", 4, "*", 2, "/", "(", 1, "-", 5, ")", "^", 2, "^", 3], [3, 4, 2, "*", 1, 5, "-", 2, 3, "^", "^", "/", "+"])
    ])
def test_shunting_yard(tokens, postfix_expression):
    s = Solution()
    assert list(s.shunting_yard(tokens)) == postfix_expression

@pytest.mark.parametrize("exp, result",[
    ([0], 0),
    ([3, 2, "+"], 5),
    ([3, 4, 2, "*", "+"], 11),
    ([3, 4, 2, "*", 1, 5, "-", 2, 3, "^", "^", "/", "+"], eval("3 + 4 * 2 / (1 - 5) ** 2 ** 3"))
    ])
def test_eval_postfix(exp, result):
    s = Solution()
    assert s.eval_postfix(exp) == result

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
