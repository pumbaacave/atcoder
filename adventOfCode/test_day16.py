from loguru import logger
from day16 import \
(parse_stmt, parse_op, FUN_LIST, count_possible_op)


TEST_INPUT1 = """\
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]
"""


def test_sample():
    lines = TEST_INPUT1.splitlines()
    i = 0
    end = len(lines)
    while(i < end):
        # line 1
        before = parse_stmt(lines[i])
        logger.debug(before)
        i += 1
        # line 2
        op = parse_op(lines[i])
        logger.debug(op)
        i += 1
        # line 3
        after = parse_stmt(lines[i])
        logger.debug(after)
        i += 1
        # line 4
        i += 1
        logger.debug(count_possible_op(before, after, op))



