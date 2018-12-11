import re
import time
import numpy as np
from loguru import logger

prog = re.compile(r"position=<(?P<x>.\d+),\s(?P<y>.\d+)>\s*velocity=<(?P<xa>.\d*),\s(?P<ya>.\d*)>$")


def parse_line(line):
    res = prog.match(line)
    return [int(res.group('x')),
            int(res.group('y')),
            int(res.group('xa')),
            int(res.group('ya')),
            ]


def print_update_chart(data):
    x_sort = sorted(data, key=lambda x:x[0])
    y_sort = sorted(data, key=lambda x:x[0])
    XMIN = x_sort[0][0]
    XMAX = x_sort[-1][0]
    YMIN = y_sort[0][0]
    YMAX = y_sort[-1][0]
    H = XMAX - XMIN
    W = YMAX - YMIN
    MEM = np.zeros((H,W), dtype='int8')
    for point in data:
        MEM[point[0]-XMIN-1][point[1]-YMIN-1] = 1
        point[0] += point[2]
        point[1] += point[3]

    print(MEM)

    return data

def run():
    with open('input10', 'r') as f:
        data = [parse_line(line.strip()) for line in f]

    while(True):
        data = print_update_chart(data)
        time.sleep(1) # sleep 1 second

run()

