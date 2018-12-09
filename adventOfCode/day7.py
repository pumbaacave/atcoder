import re
from collections import defaultdict

prog = re.compile(r".{5}(?P<head>\w).{30}(?P<tail>\w).+$")


def parse(line):
    res = prog.match(line)
    head = res.group('head')
    tail = res.group('tail')
    return [head, tail]


HEAD = '\x00'
def default_fac():
    return [HEAD]

"""
build tail -> head dict
"""
def buid_head_first(data):

    ret = defaultdict(default_fac)
    for record in data:
        ret[record[1]].append(record[0])
    return ret


def find_start(tail_to_head, head_to_tail):
    ret = []
    for k in head_to_tail:
        if k[0] not in tail_to_head.keys():
            ret.append(k[0])
    return(sorted(set(ret)))


"""
param:
    inpurt: set, list, dict
"""
def build_output(start, head_to_tail, tail_to_head):
    free = list(start)
    output = []
    while len(free) > 0:
        op = free[0]
        output.append(op)
        for k in head_to_tail:
            if k[0] != op:
                continue
            tail = k[1]
            heads = tail_to_head[tail]
            idx = heads.index(op)
            del heads[idx]
            if len(heads) == 1:
                free.append(tail)

        del free[0]
        free.sort()

    return output

def run():
    with open('input7', 'r') as f:
        head_to_tail = [parse(line.strip()) for line in f]

    tail_to_head = sorted(head_to_tail)
    print(head_to_tail)
    tail_to_head = buid_head_first(head_to_tail)
    print(tail_to_head)
    start = find_start(tail_to_head, head_to_tail)
    output = build_output(start, head_to_tail, tail_to_head)
    print(''.join(output))

TARGET = 'CFMNLOAHRKPTWBJSYZVGUQXIDE'
NUM_WORKER = 5

ORD_A = ord('A')
def cal_cost(char):
    return ord(char) - ORD_A + 61

"""
param:
    inpurt: set, list, dict
"""
def build_with_worker(start, head_to_tail, tail_to_head):
    free = list(start)
    endtime = [-1 for _ in range(NUM_WORKER)]
    now = 0
    freeable_time = defaultdict(lambda :-1)
    while len(free) > 0:
        dispatch = [*free] # copy
        print(dispatch)
        free = []
        for op in dispatch:
            # upheave sort position to maintain [0] for
            # freeable_time ceation
            endtime.sort()
            # send to worker
            print(endtime)
            print(freeable_time)
            endtime[0] = max(endtime[0], freeable_time[op])+ cal_cost(op)
            print(op)
            print(endtime)

            # find new indepandant char
            for k in head_to_tail:
                if k[0] != op:
                    continue
                tail = k[1]
                heads = tail_to_head[tail]

                idx = heads.index(op)
                del heads[idx]
                if len(heads) == 1:
                    free.append(tail)
                    freeable_time[tail] = endtime[0]

            # workers should wait for other independant char end


    return endtime

def run1():
    with open('input7', 'r') as f:
        head_to_tail = [parse(line.strip()) for line in f]

    tail_to_head = sorted(head_to_tail)
    print(head_to_tail)
    tail_to_head = buid_head_first(head_to_tail)
    print(tail_to_head)
    start = find_start(tail_to_head, head_to_tail)
    time = build_with_worker(start, head_to_tail, tail_to_head)
    print(time)

run1()
