

"""
return: the highest score of elves
"""
def cal_highest(num_player, last_marble):
    scores = [0 for i in range(num_player)]
    marbles = [0, 1]
    L = 2
    current = 1
    for i in range(2, last_marble+1):
        if i % 23 == 0:

            continue
        next_one = (current+1)//L
        next_two = (current+2)//L
        L += 1
        marbles.insert(next_two, i)
        current = next_two
