def addr(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = regs[A] + regs[B]
    return new_regs


def addi(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = regs[A] + B
    return new_regs


def mulr(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = regs[A] * regs[B]
    return new_regs


def muli(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = regs[A] * B
    return new_regs


def banr(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = regs[A] & regs[B]
    return new_regs


def bani(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = regs[A] & B
    return new_regs


def borr(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = regs[A] | regs[B]
    return new_regs


def bori(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = regs[A] | B
    return new_regs


def setr(A, _, C, regs):
    new_regs = regs[:]
    new_regs[C] = regs[A]
    return new_regs


def seti(A, _, C, regs):
    new_regs = regs[:]
    new_regs[C] = A
    return new_regs


def gtir(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = 1 if regs[A] > regs[B] else 0
    return new_regs


def gtri(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = 1 if A > B else 0
    return new_regs


def gtrr(A, B, C, regs):
    new_regs = regs[:]
    new_regs[C] = 1 if regs[A] > regs[B] else 0
    return new_regs


def parse_stmt(stmt):
    regs = []
    regs.append(int(stmt[9]))
    regs.append(int(stmt[12]))
    regs.append(int(stmt[15]))
    regs.append(int(stmt[18]))
    return regs


def parse_op(op_stmt):
    ops = []
    ops.append(int(op_stmt[0]))
    ops.append(int(op_stmt[2]))
    ops.append(int(op_stmt[4]))
    ops.append(int(op_stmt[6]))
    return ops

FUN_LIST = [addi, addr, mulr, muli, banr, bani, bori, borr, setr, seti, gtir, gtri, gtrr]

def count_possible_op(before, after, op):
    count = 0
    for f in FUN_LIST:
        if f(*op[1:], before) == after:
            count += 1
    return count
