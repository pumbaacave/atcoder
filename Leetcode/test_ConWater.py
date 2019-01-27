from ConWater import Solution

def test_1():
    Input = [1, 5]
    s = Solution()
    max_water = s.maxArea(Input)
    print(max_water)
    assert max_water == 1

def test_2():
    Input = [1, 5, 4]
    s = Solution()
    max_water = s.maxArea(Input)
    print(max_water)
    assert max_water == 4

def test_3():
    Input = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    max_water = s.maxArea(Input)
    print(max_water)
    assert max_water == 49

def test_4():
    Input = [2, 1]
    s = Solution()
    max_water = s.maxArea(Input)
    print(max_water)
    assert max_water == 1

def test_5():
    Input = [1, 2, 4, 3]
    s = Solution()
    max_water = s.maxArea(Input)
    print(max_water)
    assert max_water == 4

test_5()