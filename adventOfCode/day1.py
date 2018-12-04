def signed_str_to_int(line):
    print(line)
    return -int(line[1:]) if line[0] == '-' else int(line[1:]) if line[0] == '+' else 0


def run():
    print('start')
    with open('input1', 'r') as f:
        data = [signed_str_to_int(line.strip()) for line in f]
        print(sum(data))


run()
