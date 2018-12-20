from loguru import logger
from day16 import (parse_stmt, parse_op)


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
        logger.debug(parse_stmt(lines[i]))
        i += 1
        # line 2
        logger.debug(parse_op(lines[i]))
        i += 1
        # line 3
        logger.debug(parse_stmt(lines[i]))
        i += 1
        # line 4
        i += 1


