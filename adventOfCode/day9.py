from loguru import logger

"""
return: the highest score of elves
"""
def cal_highest(num_player, last_marble_mark):
    scores = [0 for i in range(num_player)]
    marbles = [0, 1]
    L = 2 # length of marbles list, updated dynamically
    current = 1 # current operation index
    for i in range(2, last_marble_mark+1):
        L = len(marbles)
        # logger.info(current)
        # logger.debug(marbles)
        if i % 23 == 0:
            scores, current, marbles, _L = special_op(scores, current, marbles, L, i, num_player)

            continue
        # next_one = (current+1) % L
        next_two = (current+2) if (current+2) == L else (current+2) % L
        marbles.insert(next_two, i)
        # L += 1
        current = next_two

    # assert L == len(marbles)
    return max(scores)

def special_op(scores, current, marbles, L, coming_marble_mark, num_player):
    player_on_turn = coming_marble_mark % num_player
    # add the point of coming marble
    scores[player_on_turn] += coming_marble_mark
    # supposed current >= 7
    current -= 7
    # w/o this op, once current turns into minus, later calculation will err
    current %= L
    scores[player_on_turn] += marbles[current]
    # del elem from the linked-list, now current point to clockwise-next one
    del marbles[current]
    # update length of marlbes list
    L -= 1

    return scores, current, marbles, L


