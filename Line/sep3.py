def sep(line):
    if line.find('.') >= 0:
        return line.split('.')
    else:
        return [line, None]

def process(line):
    integer, point = sep(line)
    sign = '-' if integer[0] == '-' else ''
    start = 1 if sign else 0
    L = len(integer) - start
    stack = []
    for i, s in enumerate(reversed(integer[start:])):
        stack.append(s)
        if i not in (0, L - 1) and i % 3 == 2:
            stack.append(',')
    format_int = ''.join(reversed(stack))
    if point is not None:
        return ''.join([sign, format_int, '.', point])
    else:
        return ''.join([sign, format_int])

a = process('-333333')
print(a)
