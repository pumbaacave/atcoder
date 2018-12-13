import day11
import pytest

test_data =[
        [3, 5, 8, 4],
        [122, 79, 57, -5],
        [217, 196, 39, 0],
        [101, 153, 71, 4],
        ]
@pytest.mark.parametrize("x, y, grid_serial, power", test_data)
def test_get_power_level(x, y, grid_serial, power):
    assert day11.get_power_level(x, y, grid_serial) == power
