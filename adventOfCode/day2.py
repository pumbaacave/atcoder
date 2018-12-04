def process_line(line):
    line = sorted(line)
    has_two = 0
    has_three = 0
    L = len(line)
    i = 0
    while(i < L-1 and has_two + has_three < 2):
        if (line[i] == line[i+1]):
            if( i + 2 < L and line[i+1] == line[i+2] and (i+3>=L or line[i+3] != line[i+2])):
                has_three = 1
                i += 2
            else:
                has_two = 1
                i += 1
        i += 1

    return [has_two, has_three]




def run():
    print('start')
    with open('input2', 'r') as f:
        data = [process_line(line.strip()) for line in f]
        print(data)
        sum_data = [sum(i) for i in zip(*data)]
        print(sum_data)
        print(sum_data[0]*sum_data[1])


def cal(ID):
    ret = 0
    for char in ID:
        ret += ord(char) - ord('a')
    return ret

def minor_check(str1, str2):
    one_diff = False
    target_found = False
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            continue
        elif one_diff == False:
            one_diff = True
        else:
            # encounter second diff
            return target_found

    target_found = True
    return target_found


def run1():
    print('start')
    with open('input2', 'r') as f:
        data = [line.strip() for line in f]
        chm = [cal(ID) for ID in data]
        data = sorted(data)
        # print(data)
        for i in range(len(data)-1):
            if len(data[i]) == len(data[i+1]) and chm[i+1] - chm[i] < 26:
                 if minor_check(data[i], data[i+1]):
                     print(data[i])
                     print(data[i+1])
                     print(len(data[i]))
                     break
            else:
                continue


run1()
