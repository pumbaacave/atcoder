def addr(A, B, C, regs):
    regs[C] = regs[A] + regs[B]


def addi(A, B, C, regs):
    regs[C] = regs[A] + B


def mulr(A, B, C, regs):
    regs[C] = regs[A] * regs[B]


def muli(A, B, C, regs):
    regs[C] = regs[A] * B


def banr(A, B, C, regs):
    regs[C] = regs[A] & regs[B]


def bani(A, B, C, regs):
    regs[C] = regs[A] & B


def borr(A, B, C, regs):
    regs[C] = regs[A] | regs[B]


def bori(A, B, C, regs):
    regs[C] = regs[A] | B


def setr(A, _, C, regs):
    regs[C] = regs[A]


def seti(A, _, C, regs):
    regs[C] = A


def gtir(A, B, C, regs):
    regs[C] = 1 if [A] > regs[B] else 0


def gtri(A, B, C, regs):
    regs[C] = 1 if A > B else 0


def gtrr(A, B, C, regs):
    regs[C] = 1 if regs[A] > regs[B] else 0


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
