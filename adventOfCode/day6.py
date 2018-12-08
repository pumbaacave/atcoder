import re
import bisect
import numpy

prog = re.compile(r"^(?P<x>\d+),\s(?P<y>\d+)")
def run():
    with open('temp', 'r') as f:
        p_list = []
        index = 0
        for line in f:
            res =  prog.match(line)
            x = int(res.group('x'))
            y = int(res.group('y'))
            p_list.append([x, y, index])
            index += 1

        x_list = sorted(p_list)
        y_list = sorted(zip(p_list))
        #print(p_list)
        x_min = x_list[0][0]
        x_max = x_list[-1][0]
        y_min = y_list[0][0][0]
        y_max = y_list[0][-1][0]
        print(x_min)
        print(y_min)
        start = min(x_min, y_min)
        stop = max(x_max, y_max)
        L = stop - start
        start = start - L//2 -1
        start = int(start)
        L_p = len(x_list)
        mark = numpy.zeros((2*L, 2*L), dtype='int64')
        for i in range(2*L):
            for j in range(2*L):
                dis = 4 * L
                x = start + i
                y = start + j
                # this pruning strategy not work
                # k = bisect.bisect_left(x_list, [x, y])
                k = 0
                while k< L_p:
                    # greedy stop
                    if abs(x_list[k][0]-x) > dis:
                        k += 1
                        continue
                    if abs(x_list[k][1]-y) > dis:
                        k += 1
                        continue

                    dis0 = cal(x_list[k], [x, y])
                    if dis0 < dis:
                        dis = dis0
                        mark[i][j] = k
                    elif dis0 == dis: # no count
                        mark[i][j] = 0

                    k += 1

        print(mark)
        for i in range(L_p):
            p_list[i].append(numpy.sum(mark == i))

        # clear infinite set
        for i in range(2*L):
            tar = mark[0][i]
            p_list[tar][3] = 0

            tar = mark[2*L-1][i]
            p_list[tar][3] = 0

            tar = mark[i][2*L-1]
            p_list[tar][3] = 0

            tar = mark[i][0]
            p_list[tar][3] = 0

        ret = sorted(p_list, key=lambda x:x[3])
        print(ret)


def cal(a, b):
    return(abs(a[0]-b[0])+abs(a[1]-b[1]))


def run1():
    with open('input6', 'r') as f:
        p_list = []
        index = 0
        for line in f:
            res =  prog.match(line)
            x = int(res.group('x'))
            y = int(res.group('y'))
            p_list.append([x, y, index])
            index += 1
        x_list = sorted(p_list)
        y_list = sorted(zip(p_list))
        x_min = x_list[0][0]
        x_max = x_list[-1][0]
        y_min = y_list[0][0][0]
        y_max = y_list[0][-1][0]
        start = min(x_min, y_min)
        stop = max(x_max, y_max)
        L = stop - start
        start = start - L//2 -1
        start = int(start)
        L_p = len(x_list)
        rev = list(reversed(x_list)) # list size is small, so not using generator
        print(rev)

        mark = numpy.zeros((2*L, 2*L), dtype='int64')
        area = 0
        for i in range(2*L):
            for j in range(2*L):
                total_dis = 0
                k = 0
                x = start + i
                y = start + j
                while k < L_p:
                    total_dis += cal(rev[k], [x,y])
                    if total_dis > 10000:
                        break
                    k += 1

                mark[i,j] = 1
                area = area + 1 if total_dis < 10000 else area

        print(mark)
        print(area)

run1()
