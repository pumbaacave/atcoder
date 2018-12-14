import day12
from loguru import logger

SAMPLE_RULES = '''\
...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
'''
def test_sample():
    INI_STATE = '...#..#.#..##......###...###'
    state = day12.parse_init(INI_STATE)
    rule_book = day12.parse_rules(SAMPLE_RULES)
    idx = 3
    for _ in range(20):
        idx, state = day12.next_gen(rule_book, idx, state)

    # logger.debug(state)
    assert day12.cal_point(idx, state) == 325

REAL_RULES = '''\
#.##. => .
#.#.. => .
###.# => .
..#.# => .
....# => .
.#### => .
##.## => #
###.. => #
.###. => #
...#. => .
..... => .
##..# => .
.#.#. => #
.#.## => #
##.#. => .
##... => .
##### => #
#...# => .
..##. => .
..### => .
.#... => #
.##.# => .
#.... => .
.#..# => .
.##.. => #
...## => #
#.### => .
#..#. => .
..#.. => #
#.#.# => #
####. => #
#..## => .
'''
def test_real():
    INI_STATE = '..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####'
    state = day12.parse_init(INI_STATE)
    rule_book = day12.parse_rules(REAL_RULES)
    idx = 2
    for _ in range(20):
        idx, state = day12.next_gen(rule_book, idx, state)
        # logger.debug(state)

    logger.debug(state)
    logger.debug(day12.cal_point(idx, state))
    # assert day12.cal_point(state) == 325
