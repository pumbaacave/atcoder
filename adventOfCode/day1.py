def signed_str_to_int(line):
    return -int(line[1:]) if line[0] == '-' else int(line[1:]) if line[0] == '+' else 0


def run():
    print('start')
    with open('input1', 'r') as f:
        data = [signed_str_to_int(line.strip()) for line in f]
        print(sum(data))


def run1():
    print('start')
    cur = 0
    flags = [0]
    found = False
    while not found:
        with open('input1', 'r') as f:
            for line in f:
                num = signed_str_to_int(line.strip())
                cur += num
                if cur not in flags:
                    flags.append(cur)
                else:
                    found = True
                    print(cur)
                    break


run1()
