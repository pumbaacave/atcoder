class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        A = self.arrayToInt(A)
        sum_ak = A + K
        array_ak = self.intToArray(sum_ak)
        return array_ak


    def arrayToInt(self, array):
        # empty array case covered
        integer = 0
        rev_array = reversed(array)
        for i, num in enumerate(rev_array):
            integer += num * 10 ** i
        return integer


    def intToArray(self, integer):
        target = integer
        array = []
        while target >= 10:
            div, mod = divmod(target, 10)
            array.insert(0, mod)
            target = div
        array.insert(0, target)
        return array

def test_addToArrayForm():
    s = Solution()
    A = [1, 9, 9]
    K = 1
    array = s.addToArrayForm(A, K)
    assert array[0] == 2
    assert array[1] == 0
    assert array[2] == 0

def test_intToArray():
    s = Solution()
    integer = 100
    array = s.intToArray(integer)
    assert array[0] == 1
    assert array[1] == 0
    assert array[2] == 0


def test_arrayToInt():
    s = Solution()
    array= [1, 0, 9, 9]
    integer  = s.arrayToInt(array)
    assert integer == 1099
