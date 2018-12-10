def run():
    in_list = read_input()
    # print(in_list)
    print(parse_tree(in_list))

def read_input():
    total_list = []
    with open('input8', 'r') as f:
        for line in f:
            num_list = line.split(' ')
            total_list.extend(map(int, num_list))
    return total_list

def sum_meta(in_list):
    tree_length, meta_sum = parse_tree(in_list)
    return meta_sum

def parse_tree(in_list):
    node_num = in_list[0]
    meta_num = in_list[1]
    # print("number of node:{}".format(node_num))
    # print("number of meta:{}".format(meta_num))
    if node_num == 0:
        return parse_single_node(in_list)

    children_node_length = 0
    total_meta_sum = 0
    idx = 2
    for _ in range(node_num):
        # print("tree starts at: {}".format(idx))
        tree_length, child_meta_sum = parse_tree(in_list[idx:])
        idx += tree_length
        children_node_length += tree_length
        total_meta_sum  += child_meta_sum
    # print(children_node_length)
    # print(child_meta_sum)
    for i in range(meta_num):
        meta_temp = in_list[2 + i + children_node_length]
        # print("find meta: {}, at {}".format(meta_temp, 2 + i + children_node_length))
        total_meta_sum += meta_temp

    return children_node_length + 2 + meta_num, total_meta_sum


def parse_single_node(in_list):
    node_num = in_list[0]
    meta_num = in_list[1]
    assert node_num == 0
    meta_sum = 0
    for i in range(meta_num):
        meta_temp = in_list[2 + i]
        # print("find meta: {}, at {}".format(meta_temp, 1 + i))
        meta_sum += meta_temp
    return 2 + meta_num, meta_sum


def sum_meta_alter(in_list):
    tree_length, meta_sum = parse_tree_alter(in_list)
    return meta_sum

def parse_tree_alter(in_list):
    node_num = in_list[0]
    meta_num = in_list[1]
    children_vals = []
    # print("number of node:{}".format(node_num))
    # print("number of meta:{}".format(meta_num))
    if node_num == 0:
        return parse_single_node(in_list)

    children_node_length = 0
    total_alter_sum = 0
    idx = 2
    for _ in range(node_num):
        # print("tree starts at: {}".format(idx))
        tree_length, child_alter_sum = parse_tree_alter(in_list[idx:])
        idx += tree_length
        children_node_length += tree_length
        children_vals.append(child_alter_sum)
    # print(children_node_length)
    # print(child_meta_sum)
    # calculate the sum using rules in part2
    for i in range(meta_num):
        meta_i = in_list[2 + i + children_node_length]
        if meta_i > node_num:
            pass
        else:
            total_alter_sum += children_vals[meta_i-1]

    return children_node_length + 2 + meta_num, total_alter_sum


def run1():
    in_list = read_input()
    # print(in_list)
    print(parse_tree_alter(in_list))


run1()
