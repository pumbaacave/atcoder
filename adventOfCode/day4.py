import re
import numpy
import pprint
prog = re.compile(r"^\[.{4}-(?P<month>\d+)-(?P<day>\d+)\s(?P<hour>\d+):(?P<min>\d+)\]\s(?P<selector>\w{5})\s(?P<state>.+)$")
id_matcher = re.compile(r"^#(?P<id>\d+)\s.+$")


def parse(line):
    res = prog.match(line)
    return [int(res.group('month')),
            int(res.group('day')),
            int(res.group('hour')),
            int(res.group('min')),
            res.group('selector'),
            res.group('state')]


def sumSleepTime(data):
    summary = {}
    gen = (record for record in data)
    ID = ''  # initialisation
    try:
        while(True):
            record = next(gen)
            if (record[4] == 'Guard'):
                # str
                ID = id_matcher.match( record[5]).group('id')
                if ID not in summary:
                    summary[ID] = numpy.zeros(60)
            else:
                sleep = record[3]
                wake = next(gen)[3]
                summary[ID][sleep:wake] += 1

            continue

    except Exception as E:
        print("summary end")
    return summary


def findSleepyGuard(summary):
    sort_s = sorted(summary.items(), key=lambda x: numpy.sum(x[1]), reverse=True)
    a = sort_s[0][0]
    b = max(sort_s[0][1])
    print(sort_s[0])
    print(sort_s[1])
    print(a)
    print(b)
    c = numpy.where(sort_s[0][1] == b)
    print(c)
    print(int(a) * (int(c[0]))) # +1 is not needed, because


def run():
    print('start')
    with open('input4', 'r') as f:
        data = [parse(line.strip()) for line in f]

    #  pprint.pprint(sorted(data))
    summay = sumSleepTime(sorted(data))
    findSleepyGuard(summay)


def sumSleepFreq(data):
    summary = {}
    gen = (record for record in data)
    ID = ''  # initialisation
    try:
        while(True):
            record = next(gen)
            if (record[4] == 'Guard'):
                # str
                ID = id_matcher.match( record[5]).group('id')
                if ID not in summary:
                    summary[ID] = 0
            else:
                sleep = record[3]
                wake = next(gen)[3]
                summary[ID] += (wake - sleep)

            continue

    except Exception as E:
        print("summary end")
    return summary


def findFrequentSleepGuard(summary):
    sort_s = sorted(summary.items(), key=lambda x: max(x[1]), reverse=True)
    a = sort_s[0][0]
    b = max(sort_s[0][1])
    print(a)
    print(b)
    c = numpy.where(sort_s[0][1] == b)
    print(c)
    print(int(a) * (int(c[0]))) # +1 is not needed, because

def run1():
    print('start')
    with open('input4', 'r') as f:
        data = [parse(line.strip()) for line in f]

    #  pprint.pprint(sorted(data))
    summay = sumSleepTime(sorted(data))
    pprint.pprint(summay)
    findFrequentSleepGuard(summay)


run1()

