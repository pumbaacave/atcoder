# import sys
# stdin = sys.stdin
# def li(): return map(int, stdin.readline().split())
# N, M = tuple(li())
# nums = tuple(li())

def get_larger_digits_same_len(cur, d):
    sorted_cur = sorted(cur, reverse=True)
    sorted_d = sorted(d, reverse=True)
    for i, j in zip(sorted_cur, sorted_d):
        if i > j:
            return sorted_cur
        elif i < j:
            return sorted_d
    # case equal
    return cur

def test_get_larger_digits_same_len():
    a = [1, 2, 3]
    b = [1, 4, 3]
    ans = get_larger_digits_same_len(a, b)
    ans = tuple(ans)
    assert ans == (4, 3, 1)


def get_larger_digits(cur, digits, new_digits):
    if not digits:
        return cur
    d = digits[:]
    d.extend(new_digit)
    if len(d) > len(cur):
        return d
    elif len(d) < len(cur):
        return cur
    else:
        # case equal lengths
        return get_larger_digits_same_len(cur, d)

def test_get_larger_digits1():
    a = [1, 3, 5]
    b = [1, 3, 5, 0]
    ans = get_larger_digits(a, b, [1])
    assert len(ans) == 5

def test_get_larger_digits_one_empty_list():
    a = []
    b = [1, 3, 5, 0]
    ans = get_larger_digits(a, b, [1])
    assert len(ans) == 5

cost_dict ={
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6,
        }
# init
init = [[]] * 8 # idx from 0 to 7
for i in range(8):
    cur = []
    for num in nums:
        if i - cost_dict[num] < 0:
            continue
        elif i == cost_dict[num]:
            cur = get_larger_digits(cur, [], [num])
        elif i > cost_dict[num] and init[i - cost_dict[num]]:
            cur = get_larger_digits(cur, init[i-cost_dict[num]], [num])
    init[i] = cur

state = reversed(init)
state = init_state = list(state)
print(state)


for _ in range(N-7):
    cur = []
    for cost, nums in enumerate(init):
        cur = get_larger_digits(cur, state[cost-1], nums)
    state = [cur] + state[:-1]
print("".join(map(str, sorted(state[0], reverse=True))))
