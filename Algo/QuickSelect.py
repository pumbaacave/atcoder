import pytest
import pytest_benchmark
from hypothesis import given
from hypothesis.strategies import lists, integers
from loguru import logger
import random
def partition(nums, left, right, pivot_idx):
    # partition nums[left:right+1] into greater then(gt) and less or equal(leq) part on pivot_val
    # leq part reside on nums[left:store_idx]
    pivot_val = nums[pivot_idx]
    nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
    store_idx = left
    # exclude nums[right]
    for i in range(left, right):
        if nums[i] <= pivot_val:
            nums[store_idx], nums[i] = nums[i], nums[store_idx]
            store_idx += 1

    # swap pivot_val to corresond place
    nums[store_idx], nums[right] = nums[right], nums[store_idx]
    # logger.debug(nums)
    return store_idx

def quick_select(nums, left, right, K):
    # return the Kth large element of nums
    # pivot_idx = random.randrange(left, right+1)
    pivot_idx = right
    partition_idx = partition(nums, left, right, pivot_idx)
    if partition_idx == K:
        return nums[partition_idx]
    elif partition_idx > K:
        return quick_select(nums, left, partition_idx-1, K)
    else:
        return quick_select(nums, partition_idx+1, right, K-partition_idx)


@pytest.mark.skip()
@given(nums=lists(integers(), 1))
def test_partition(nums):
    L = len(nums)
    left, right = 0, len(nums) - 1
    pivot_idx = random.randrange(left, right+1)
    partition_idx = partition(nums, left, right, pivot_idx)
    logger.debug(nums)
    assert partition_idx == 0 or nums[partition_idx] >= max(nums[:partition_idx])
    # assert nums[:partition_idx] == sorted(nums[:partition_idx])


@pytest.mark.skip()
@given(nums=lists(integers(), 1))
def test_quick_select(nums):
    left, right = 0, len(nums) - 1
    K = 0
    val = quick_select(nums, left, right, K)
    logger.debug(nums)
    assert nums[K] == val


import sys
from timeit import default_timer, timeit
sys.setrecursionlimit(100*1000)
#@pytest.mark.skip()
@pytest.mark.parametrize("size",[1000 * i for i in range(1, 10)])
def test_time(size):
    nums = list(range(size))
    random.shuffle(nums)
    left, right = 0, size - 1
    K = random.randrange(left, right+1)
    
    # start = default_timer()
    # ans = quick_select(nums, left, right, K)
    # end = default_timer()
    # print(globals())
    print(timeit("ans = quick_select(nums, left, right, K)", globals=globals().update(locals())), size)
    # logger.debug(f"problem size: {size}, time: {end - start}")
    assert ans == K

