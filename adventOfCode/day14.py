def update_recipe(pos1, pos2, state):
    new_recipe = state[pos1] + state[pos2]
    q, r = divmod(new_recipe, 10)
    if q > 0:
        state.append(q)
    state.append(r)
    l = len(state)
    pos1 = move(pos1, state[pos1], l)
    pos2 = move(pos2, state[pos2], l)
    return pos1, pos2, state


def move(start, steps, space):
    next_pos = start + steps + 1
    next_pos %= space
    return next_pos

