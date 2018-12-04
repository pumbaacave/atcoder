import re
import numpy
prog = re.compile(r"^#(?P<id>\d+)\s@\s(?P<x>\d+),(?P<y>\d+):\s+(?P<w>\d+)x(?P<h>\d+)")
def parse(line):
    res = prog.match(line)
    return [res.group('id'),
            res.group('x'),
            res.group('y'),
            res.group('w'),
            res.group('h')]


def paste(claims):
    fibre = numpy.zeros((1001, 1001), dtype='int64')
    for c in claims:
        fibre[c[1]:c[1]+c[3], c[2]:c[2]+c[4]] += 1
    return fibre

def run():
    print('start')
    with open('input3', 'r') as f:
        data = [list(map(int, parse(line.strip()))) for line in f]
    fibre = paste(data)
    print(fibre)
    SUM = numpy.sum(fibre > 1)
    print(SUM)


def find_nonconflict_claim(hitmap, claims):
    for c in claims:
        sum_of_target_area = numpy.sum(hitmap[c[1]:c[1]+c[3], c[2]:c[2]+c[4]])
        if sum_of_target_area == c[3] * c[4]:
            return c[0]


def run1():
    print('start')
    with open('input3', 'r') as f:
        claims = [list(map(int, parse(line.strip()))) for line in f]
    fibre = paste(claims)
    hitmap = fibre == 1
    key = find_nonconflict_claim(hitmap, claims)
    print(key)


run1()
