"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

"""
import mathext
import math
from loguru import logger


def get_trail_zero(fac):
    count = 0
    while True:
        div, mod = divmod(fac, 10)
        if mod == 0:
            count += 1
            fac = div
        else:
            return count

def get_cal_zero(n):
    if n == 0:
        return 0
    exp_five = math.log(n, 5)
    exp_five = int(exp_five)
    zero_count = 0
    for i in range(exp_five):
        target = math.pow(5, i + 1) # 5, 25, 125, ...
        zero_count += n // target
    return count


i = 1
fac = 1
while True:
    # fac = mathext.factorial(i)
    fac = fac * i
    trail_zero = get_trail_zero(fac)
    cal_zero = get_cal_zero(i)
    if cal_zero != trail_zero:
        logger.debug(i)
        logger.debug(fac)
        break
    i += 1
    if i % 10 == 0:
        logger.debug(f'now test throug {i}')


