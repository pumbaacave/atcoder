import random

def helper(nums, l, r, pivot):
    if l >= r:
        return
    # swap pivot to right
    val_pivot = nums[pivot]
    nums[pivot], nums[r] = nums[r], nums[pivot]
    swap_idx = l
    for i in range(l, r):
        if nums[i] < val_pivot:
            nums[swap_idx], nums[i] = nums[i], nums[swap_idx]
            swap_idx += 1
    # swap pivot with first elem larger than pivot
    nums[swap_idx], nums[r] = nums[r], nums[swap_idx]
    helper(nums, l, swap_idx - 1, swap_idx - 1)
    helper(nums, swap_idx + 1, r, r)


def quicksort(nums):
    if not nums: return ()
    l, r = 0, len(nums) - 1
    pivot = random.randint(l, r)
    helper(nums, l, r, pivot)
    return nums

def test_sort_empty():
    nums = []
    ans = quicksort(nums)
    assert tuple(ans) == tuple()

def test_sort_float():
    nums = [1, 1.0, 2, 2.0, 3.0, 3, 4.0, 4]
    ans = quicksort(nums)
    assert tuple(ans) == (1, 1.0, 2.0, 2, 3, 3.0, 4, 4.0)

def test_sort():
    nums = [3, 2, 8, 33, 10, -3, 999, -124, 33]
    ans = quicksort(nums)
    assert tuple(ans) == (-124, -3, 2, 3, 8, 10, 33, 33, 999)
