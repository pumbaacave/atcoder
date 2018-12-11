import pytest
import day9

test_data =[
        [9, 25, 32],
        [10, 1618, 8317],
        [13, 7999, 146373],
        [17, 1104, 2764],
        [21, 6111, 54718],
        [30, 5807, 37305]
        ]
@pytest.mark.parametrize("num_player, last_marble, highest_score", test_data)
def test_marble(num_player, last_marble, highest_score):
    assert day9.cal_highest(num_player, last_marble) == highest_score
