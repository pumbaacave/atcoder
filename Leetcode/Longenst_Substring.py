# from loguru import logger
from collections import defaultdict

# def debug(*args):
#     logger.debug(args)


def update_char_stat(word, char_stat, max_middle_len):
    if not word:
        return char_stat, max_middle_len
    former = word[0]
    counter = 0
    char_first_changed = True
    head = -1
    tail = -1
    # TODO: can only update either head or tail once
    for i, char in enumerate(word):
        if char == former:
            counter += 1
        else:
            if char_first_changed: 
                # flip the flag
                char_first_changed = False
                head = char_stat[former].get('head')
                head = head if head else 0
                if word[0] != word[-1]:
                    char_stat[former]['head'] = max(head, counter)
                # else head update will be delayed to wait for tail
                else:
                    head = counter


                # reset counter for max_middle_len update
                former = char
                counter = 1
            else:
                max_middle_len = max(max_middle_len, counter)
                counter = 1
                former = char

    # head and tail exists
    if not char_first_changed:
        tail = char_stat[former].get('tail')
        tail = tail if tail else 0
        if word[0] != word[-1]:
            char_stat[former]['tail'] = max(tail, counter)
        else:
            ori_head = char_stat[former].get('head')
            ori_head = ori_head if ori_head else 0
            ori_tail = char_stat[former].get('tail')
            ori_tail = ori_tail if ori_tail else 0
            if head - ori_head > counter - ori_tail:
                char_stat[former]['head'] = head
            else:
                char_stat[former]['tail'] = tail

    if char_first_changed:
        pure = getattr(char_stat[former], 'pure', [])
        pure.append(counter)
        char_stat[former]['pure'] = pure

    return char_stat, max_middle_len


def max_cat_subsequence(char_stat):
    max_len = 0
    for _, single_stat in char_stat.items():
        head = single_stat['head'] if single_stat.get('head') else 0
        pure = single_stat['pure'] if single_stat.get('pure') else []
        tail = single_stat['tail'] if single_stat.get('tail') else 0
        temp_len = head + tail + sum(pure)
        max_len = max(max_len, temp_len)
    return max_len



def solution(words):
    # write your code in Python 3.6
    if not words:
        return 0

    char_stat = defaultdict(dict)
    max_middle_len = 0

    for word in words:
        char_stat, max_middle_len = update_char_stat(word, char_stat, max_middle_len)
    return max(max_middle_len, max_cat_subsequence(char_stat))


def test_char_update():
    char_stat = defaultdict(dict)
    max_middle_len = 0
    word = "aabbaa"

    char_stat, max_middle_len = update_char_stat(word, char_stat, max_middle_len)
    assert max_middle_len == 2
    assert char_stat['a']['head'] == 2
    assert char_stat['a']['tail'] == 2

def test_multi_char_update():
    char_stat = defaultdict(dict)
    max_middle_len = 0
    words = ['x', 'xbx', 'xxbxx']

    for word in words:
        char_stat, max_middle_len = update_char_stat(word, char_stat, max_middle_len)
    assert max_middle_len == 1
    assert char_stat['x']['head'] == 2
    assert char_stat['x']['tail'] == 2
    assert char_stat['x']['pure'] == [1]
    result = max(max_middle_len, max_cat_subsequence(char_stat))
    assert result == 5


test_multi_char_update()


def test_char_update_pure():
    char_stat = defaultdict(dict)
    max_middle_len = 0
    word = "aaaa"

    char_stat, max_middle_len = update_char_stat(word, char_stat, max_middle_len)
    assert max_middle_len == 0
    assert char_stat['a']['pure'] == [4]

def test_cal():
    dt = {'a':
            {
            'head':4,
            'pure':[2]
            },
    }
    ans =  max_cat_subsequence(dt)
    assert ans == 6