import day8
def test_sum_meta():
    IN = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    assert day8.sum_meta(IN) == 138


def test_sum_meta_alter():
    IN = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    assert day8.sum_meta_alter(IN) == 66
