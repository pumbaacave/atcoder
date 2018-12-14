import re
from loguru import logger

INI_STATE = '..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####'
# INI_STATE = '...#..#.#..##......###...###'
prog = re.compile(r"(?P<key>.{5})\s=>\s(?P<value>.)$")

def parse_init(init_str):
    state = []
    for i in range(len(init_str)):
        if init_str[i] == '.':
            state.append(0)
        else:
            state.append(1)

    return state


def parse_rules(input_str):
    gen_plant_book = {}
    #  with open('input12', 'r') as f:
    #      for line in f:
    #          add_rule(line.strip(), gen_plant_book)
    for line in input_str.splitlines():
        add_rule(line.strip(), gen_plant_book)
    logger.debug(gen_plant_book.keys())
    return gen_plant_book


def add_rule(line, rule_book):
    res = prog.match(line)
    key = parse_key(res.group('key'))
    val = 1 if res.group('value') == '#' else 0
    # assume noe key conflict
    # if search is too slow can alter to sorted list
    if val == 1:
        rule_book[key] = val


# len(key_str) == 5
def parse_key(key_str):
    key = 0
    for i in range(len(key_str)):
        if key_str[i] == '#':
            key += 2 ** i
    return key

def parse_key_int(int_list):
    key = 0
    assert len(int_list) == 5
    for i in range(len(int_list)):
        if int_list[i] == 1:
            key += 2 ** i
    return key

def next_gen(rule_book, start_idx, state):
    start_idx += 2

    state.insert(0, 0)
    state.insert(0, 0)
    state.append(0)
    state.append(0)
    state_len = len(state)
    state.insert(0, 0)
    state.insert(0, 0)
    state.append(0)
    state.append(0)

    next_state = [0 for _ in range(state_len)]
    for i in range(2, state_len+2):
        key = parse_key_int(state[i-2:i+3])

        # logger.debug(f"elem: {i}: key:{key}")
        if key in rule_book.keys():
            next_state[i-2] = 1

    return start_idx, next_state


def cal_point(idx, state):
    SUM = 0
    l = len(state)
    for i in range(l):
        if state[i] == 1:
            SUM += (i - idx)

    return SUM


def run():
    state = parse_init(INI_STATE)
    # add dummy head for state[-2], state[-1]
    rule_book = parse_rules()
    for _ in range(20):
        state = next_gen(rule_book, 3, state)
        logger.debug(state)

    cal_point(state)


