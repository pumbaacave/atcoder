class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        if X >= Y:
            return X - Y
        else:
            ans = 0
            while Y > X:
                if Y % 2 == 0:
                    ans += 1
                    Y /= 2
                else:
                    ans += 2
                    Y = (Y+1)/2
            return ars + X - Y


        # self.entered[X] = True
        # if X >= Y:
        #     return X - Y
        # 
        # elif X in self.state.keys():
        #     return self.state[X]
        # else:

        #     if 2*X not in self.state:
        #         if 2*X not in self.entered:
        #             double = self.brokenCalc(2*X, Y)
        #         else:
        #             double = 1 << 100
        #     else:
        #         double = self.state[2*X]

        #     if X-1 not in self.state:
        #         if X-1 not in self.entered:
        #             decr = self.brokenCalc(X-1, Y)
        #         else:
        #             decr = 1 << 100
        #     else:
        #         decr = self.state[X-1]
        #     cost =  min(double, decr) + 1
        #     self.state[X] = cost
        #     return cost

def test1():
    s = Solution()
    X = 2
    Y = 3
    ans = s.brokenCalc(X, Y)
    assert ans == 2

def test2():
    s = Solution()
    X = 5
    Y = 8
    ans = s.brokenCalc(X, Y)
    assert ans == 2

def test3():
    s = Solution()
    X = 1
    Y = 1000000000
    ans = s.brokenCalc(X, Y)
    assert ans == 3
