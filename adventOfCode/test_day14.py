import day14
import pytest
from loguru import logger

def test_move():
    start = 1
    steps = 7
    space = 6
    assert day14.move(start, steps, space) == 3


test_data =[
        [[3,7], 9, [5,1,5,8,9,1,6,7,7,9]],
        [[3,7], 5, [0,1,2,4,5,1,5,8,9,1]],
        [[3,7], 18, [9,2,5,1,0,7,1,0,8,5]],
        [[3,7], 2018, [5,9,4,1,4,2,9,8,8,2]],
        ]
@pytest.mark.parametrize("ini, rounds, follow_ten_res", test_data)
def test_sample(ini, rounds, follow_ten_res):
    pos1 = 0
    pos2 = 1
    state = ini
    for _ in range(rounds+12):
        pos1, pos2, state= day14.update_recipe(pos1, pos2, state)

    assert state[rounds:rounds+10] == follow_ten_res


def test_real():
    rounds = 77201
    ini = [3, 7]
    pos1 = 0
    pos2 = 1
    state = ini
    for _ in range(rounds+12):
        pos1, pos2, state= day14.update_recipe(pos1, pos2, state)
    logger.debug(state[rounds:rounds+10])

def test_real():
    rounds = 77201
    ini = [3, 7]
    pos1 = 0
    pos2 = 1
    state = ini
    target = [0,7,7,2,0,1]
    for _ in range(12):
        pos1, pos2, state= day14.update_recipe(pos1, pos2, state)
    while True:
        pos1, pos2, state= day14.update_recipe(pos1, pos2, state)
        if state[-6:] == target:
            logger.debug(len(state))
            break
        elif state[-7:-1] == target:
            logger.debug(len(state)-1)
            break


